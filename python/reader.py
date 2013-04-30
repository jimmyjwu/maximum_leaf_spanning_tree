import config
import graph

import re

NUMBER_FORMAT_REGEXP = [None
        , re.compile('^(\d+)\n?')
        , re.compile('^(\d+) (\d+)\n?')]
NUMBER_EXPECTED_MESSAGE = [None
        , 'Expecting one natural number on a line with no leading or trailing spaces.'
        , 'Expecting two natural numbers separated by a single space on a line with no leading or trailing spaces.']

class ReaderException(BaseException):
    def __init__(self, line_num, case_num, line, message):
        self.line_num = line_num
        self.case_num = case_num
        self.line = line
        self.message = message

    def __str__(self):
        return "Error on line {0}{1}: Got '{2}'. {3}".format(
                self.line_num, self.case_info(), self.line, self.message)

    def case_info(self):
        if self.case_num == 0:
            return ""
        return ' (Graph #{0})'.format(self.case_num)

class Reader:
    def __init__(self, file_obj):
        self.file_obj = file_obj
        self.line_num = 0
        self.case_num = 0
        self.line = None

    def readline(self):
        self.line_num += 1
        self.line = self.file_obj.readline()

    def stripped_line(self):
        if self.line_num > 0 and len(self.line) > 0 and self.line[-1] == '\n':
            return self.line[:len(self.line)-1]
        return self.line

    def exception(self, message):
        return ReaderException(self.line_num, self.case_num,
                self.stripped_line(), message)

    def exception_with_expected(self, message, expected):
        return self.exception(message + ' ' + expected)

    def read_numbers(self, message, n):
        try:
            self.readline()
        except IOError as e:
            raise self.exception('{0} ({1})'.format(message, e),
                    'Expecting the next line.')

        matches = NUMBER_FORMAT_REGEXP[n].match(self.line)
        if not matches:
            raise self.exception_with_expected(message,
                    NUMBER_EXPECTED_MESSAGE[n])

        nums = []
        for i in range(n):
            try:
                nums.append(int(matches.group(i+1)))
            except ValueError as e:
                raise self.exception_with_expected('{0} ({1})'.format(message,
                    e), NUMBER_EXPECTED_MESSAGE[n])
        return nums

class InFileReader(Reader):
    def read_input_file(self):
        nums = self.read_numbers('Cannot parse the number of input graphs.', 1)

        num_cases = nums[0]
        edge_sets = []
        for i in range(num_cases):
            self.case_num = i+1
            es = self.read_input_graph()

            G = graph.make_graph(es)
            G.search()
            if not G.edges_in_one_component():
                raise self.exception('Disconnected graph: after reading '+
                'the last edge of this graph, the edges are not in '+
                'the same component.')

            edge_sets.append(es)

        self.case_num += 1
        self.readline()
        if len(self.line) > 0:
            raise self.exception_with_expected('Extra lines after Graph ' +
                    '#{0} (line 1 says the number of graphs is {0}).'.
                    format(num_cases), 'Expecting EOF.')

        return edge_sets

    def read_input_graph(self):
        nums = self.read_numbers('Cannot parse the number of edges.', 1)

        num_edges = nums[0]
        if num_edges > config.MAX_NUM_EDGES:
            raise self.exception('Number of edges cannot '+
                    'exceed {0}.'.format(config.MAX_NUM_EDGES))

        edge_set = set()
        for i in range(num_edges):
            nums = self.read_numbers('Cannot parse the next edge.', 2)
            e = graph.Edge(nums[0], nums[1])

            try:
                e.check()
            except graph.EdgeException as ex:
                raise self.exception(str(ex))

            if e in edge_set:
                raise self.exception(('Edge {0} (or its reverse) '+
                'is duplicated.').format(e))

            edge_set.add(e)

        return edge_set

class OutFileReader(Reader):
    def read_output_file(self, edge_sets):
        nums = self.read_numbers('Cannot parse the number of output graphs.', 1)

        if nums[0] != len(edge_sets):
            raise self.exception(('The number of output graphs ({0}) should '+
                    'equal the number of input graphs ({1}).').format(
                        nums[0], len(edge_sets)))

        num_cases = len(edge_sets)
        num_leaves = []

        for i in range(num_cases):
            self.case_num = i+1
            num_leaves.append(self.read_output_graph(edge_sets[i]))

        self.case_num += 1
        self.readline()
        if len(self.line) > 0:
            raise self.exception_with_expected('Extra lines after Graph ' +
                    '#{0} (line 1 says the number of graphs is {0}).'.
                    format(num_cases), 'Expecting EOF.')

        return num_leaves

    def read_output_graph(self, in_edge_set):
        nums = self.read_numbers('Cannot parse the number of edges.', 1)

        Gin = graph.make_graph(in_edge_set)
        Gin.search()
        if nums[0] != Gin.num_nodes-1:
            raise self.exception(('Input graph has {0} non-isolated '+
                    'nodes, output graph should have {1} edges, '+
                    'got {2} instead.').format(Gin.num_nodes, Gin.num_nodes-1,
                        nums[0]))

        out_edge_set = set()
        num_edges = nums[0]
        for i in range(num_edges):
            nums = self.read_numbers('Cannot parse the next edge.', 2)
            e = graph.Edge(nums[0], nums[1])

            if e not in in_edge_set:
                raise self.exception(('Edge {0} in the output graph is '+
                'absent in the input graph.').format(e))

            if e in out_edge_set:
                raise self.exception(('Edge {0} (or its reverse) is '+
                'duplicated.').format(e))

            out_edge_set.add(e)

        Gout = graph.make_graph(out_edge_set)
        Gout.search()
        if Gout.num_nodes != Gin.num_nodes:
            raise self.exception(('After reading the last edge, the number '+
                    'of non-isolated nodes in the output graph ({0}) '+
                    'should equal that of the input graph ({1}) to be '+
                    'a spanning tree.').format(Gout.num_nodes, Gin.num_nodes))
        if not Gout.edges_in_one_component:
            raise self.exception('Disconnected graph: after reading the last edge, the output graph should be connected to be a spanning tree.')
        if Gout.has_cycle:
            raise self.exception('Cycle detected: after reading the last edge, the output graph should not have cycles to be a spanning tree.')

        return Gout.num_leaves
