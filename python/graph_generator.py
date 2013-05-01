from graph import *
from random import shuffle

"""
Our objective is to build a "hard instance" graph such that our output spanning
tree for the graph has more leaves than the outputs that anyone else achieves
on the same graph (using their algorithms).

Since the three "hard instances" are due much earlier than the algorithm, we
generate hard instances in the following way:
- Create a leafy tree (goes into hard.out).
- Obscure this tree by adding unnecessary edges (goes into hard.in).

We conjecture (but cannot prove) that if we impose certain conditions on the
generation of this graph, then the tree we built will be the MLST for the graph
(or at least an exceptionally leafy tree).
"""


# Returns a hard graph instance
def create_hard_graph(number_of_nodes):
	leafy_tree = create_leafy_tree(number_of_nodes)
	hard_graph = graph_containing_tree(leafy_tree)

	return hard_graph


# Returns a tree with many leaves
def create_leafy_tree(number_of_nodes):

	# Create an empty graph
	tree = Graph(number_of_nodes)

	# Maintain a random-ordered list of unused leaves
	unused_leaves = [i for i in range(1, number_of_nodes)]
	shuffle(unused_leaves)


	# Define a helper function to recursively build the tree
	def build_leafy_tree(root_node, number_of_nodes):
		# Create some leaves

		# Branch out by recursively calling build_leafy_tree()



		return


	# Populate the tree with appropriate edges
	build_leafy_tree(0, number_of_nodes)


	return tree



# Takes a tree and returns a general graph that contains the tree and obscures its leaves.
def graph_containing_tree(tree):

	# Maintain a random-ordered list of unused edges
	unused_edges = get_unused_edges(tree)
	shuffle(unused_edges)

	# Add random edges to tree to obscure its leaves


	return tree

# Returns a list of edges in the graph
def get_edges(graph):
	number_of_nodes = len(graph.neighbors)
	edge_set = set()

	for current_node in range(0, number_of_nodes):
		for adjacent_node in graph.neighbors[current_node]:
			edge_set.add(Edge(current_node, adjacent_node))

	return list(edge_set)


# Returns a list of edges not used in the graph.
def get_unused_edges(graph):
	number_of_nodes = len(graph.neighbors)
	unused_edge_set = set()

	for current_node in range(0, number_of_nodes):
		current_node_neighbors = set(graph.neighbors[current_node])
		for other_node in range(0, number_of_nodes):
			if current_node != other_node:
				if other_node not in current_node_neighbors:
					unused_edge_set.add(Edge(current_node, other_node))

	return list(unused_edge_set)


# Returns a random graph of given size
def create_sample_graph(number_of_nodes, number_of_edges):

	# For an undirected graph with n nodes, m = n(n-1)/2
	if number_of_edges > number_of_nodes * (number_of_nodes - 1) / 2:
		number_of_edges = number_of_nodes * (number_of_nodes - 1) / 2

	# Create empty graph
	sample_graph = Graph(number_of_nodes)

	# Maintain a random-order list of unused edges
	unused_edges = get_unused_edges(sample_graph)
	shuffle(unused_edges)

	# Add random edges to graph
	for _ in range(number_of_edges):
		sample_graph.add_edge(unused_edges.pop())

	return sample_graph


# Outputs several graphs to a text file in the format given by instructors
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



