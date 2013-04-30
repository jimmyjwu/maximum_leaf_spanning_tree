import config

class EdgeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Edge:
    def __init__(self, u, v):
        self.ends = [min(u, v), max(u, v)]

    def __str__(self):
        return '({0},{1})'.format(self.ends[0], self.ends[1])

    def __hash__(self):
        return self.ends[0] * config.MAX_NUM_NODES + self.ends[1]

    def __cmp__(self):
        return object.__cmp__(self)

    def __eq__(self, rhs):
        return self.ends[0] == rhs.ends[0] and self.ends[1] == rhs.ends[1]

    def check(self):
        for i in range(2):
            if self.ends[i] < 0 or self.ends[i] >= config.MAX_NUM_NODES:
                raise EdgeException(('Node {0} out of range [0--{1}] '+
                    'in edge {2}.').format(self.ends[i], MAX_NUM_NODES-1,
                        self))
        if self.ends[0] == self.ends[1]:
            raise EdgeException('Self-loop not allowed in '+
                    'edge {0}.'.format(self))

def make_graph(edge_set):
    G = Graph(config.MAX_NUM_NODES)

    for e in edge_set:
        G.add_edge(e)

    return G

class Graph:
    def __init__(self, numNodes):
        self.neighbors = [ [] for i in range(config.MAX_NUM_NODES) ]
        self.num_of_components = 0
        self.num_nodes = 0
        self.num_leaves = 0
        self.has_cycle = False

    def add_edge(self, e):
        self.add_edge_uv(e.ends[0], e.ends[1])

    def add_edge_uv(self, u, v):
        self.add_directed_edge_uv(u, v)
        self.add_directed_edge_uv(v, u)

    def add_directed_edge_uv(self, u, v):
        self.neighbors[u].append(v)

    def edges_in_one_component(self):
        return self.num_of_components == 1

    def search(self):
        visited = [ False for i in range(config.MAX_NUM_NODES) ]
        self.num_nodes = 0
        self.num_leaves = 0
        self.num_of_components = 0
        self.has_cycle = False

        def dfs(node, parent):
            visited[node] = True
            for u in self.neighbors[node]:
                if u != parent:
                    if not visited[u]:
                        dfs(u, node)
                    else:
                        self.has_cycle = True

        for i in range(len(self.neighbors)):
            if len(self.neighbors[i]) > 0:
                self.num_nodes += 1
                if len(self.neighbors[i]) == 1:
                    self.num_leaves += 1
                if not visited[i]:
                    self.num_of_components += 1
                    dfs(i, -1)
