from graph import *
from graph_helper import *
from constants import *
from collections import deque

"""
This file contains functions for reading graphs from files and writing them to files.
"""

# Reads and returns all graphs in the given text file
# NOTE: Graphs must be in format given by instructors
def input_graphs_from_file(file_name):

	# Read in raw lines
	with open(file_name) as input_file:
		raw_lines = input_file.readlines()

	# Strip newline from each line
	for i in range(len(raw_lines)):
		raw_lines[i] = raw_lines[i].strip()

	# Store lines in a queue (using deque) for efficient processing
	lines = deque(raw_lines)

	# Maintain a list of graphs
	graphs = []

	# Read the number of graphs in file
	if len(lines) > 0:
		number_of_graphs = int(lines.popleft())
	else:
		return []

	# Read lines in nested structure
	for _ in range(number_of_graphs):
		edges = []
		number_of_edges = int(lines.popleft())

		for _ in range(number_of_edges):
			edge_ends = lines.popleft().split()
			u = int(edge_ends[0])
			v = int(edge_ends[1])
			edges.append(Edge(u, v))

		graph = make_graph(edges)
		graphs.append(graph)

	return graphs


# Outputs several graphs to a text file in the format given by instructors
# NOTE: Overwrites existing file with same name
def output_graphs_to_new_file(graphs, file_name):
	output_file = open(file_name, 'w')

	number_of_graphs = len(graphs)
	output_file.write(str(number_of_graphs) + '\n')

	for graph in graphs:
		output_graph_to_existing_file(graph, output_file)

	output_file.close()


# Outputs the graph to a text file in the format given by instructors
def output_graph_to_existing_file(graph, output_file):

	# Build a list of distinct edges
	edges = get_edges(graph)

	# Output number of edges in this graph to file
	number_of_edges = len(edges)
	output_file.write(str(number_of_edges) + '\n')

	# Output all the edges in this graph to file
	for edge in edges:
		u = edge.ends[0]
		v = edge.ends[1]
		output_file.write(str(u) + ' ' + str(v) + '\n')

# Merges best solutions from two files into a single new file
# NOTE: the tree at index i of File 1 must correspond to the tree at index i of File 2
def merge_solutions(file_name_1, file_name_2, merged_file_name):
	trees_1 = input_graphs_from_file(file_name_1)
	trees_2 = input_graphs_from_file(file_name_2)

	for tree in trees_1:
		tree.search()
	for tree in trees_2:
		tree.search()

	best_trees = []
	for i in range(len(trees_1)):
		if trees_1[i].num_leaves >= trees_2[i].num_leaves:
			best_trees.append(trees_1[i])
			print('Best tree for graph ' + str(i) + ' is in file 1.')
		else:
			best_trees.append(trees_2[i])
			print('Best tree for graph ' + str(i) + ' is in file 2.')

	output_graphs_to_new_file(best_trees, merged_file_name)

