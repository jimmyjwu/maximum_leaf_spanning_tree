from graph import *
from random import shuffle, randint

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

# Define constants
MAXIMUM_DEGREE = 5
CONSTANT_CONSTRUCTION = 1234
RANDOM_CONSTRUCTION = 2345


# Returns a hard graph instance
def create_hard_graph(number_of_nodes, construction_type):

	# Define the degree function for constant tree construction
	def get_constant_branch_and_leaf_factors():
		branch_factor = 4
		leaf_factor = 5
		return [branch_factor, leaf_factor]

	# Define the degree function for randomized tree construction
	def get_randomized_branch_and_leaf_factors():
		degree = randint(2, MAXIMUM_DEGREE)
		random_factor = random(1, degree)
		leaf_factor = max(random_factor, degree - random_factor)
		branch_factor = degree - leaf_factor
		return [branch_factor, leaf_factor]

	# Select the correct degree function
	degree_function = None
	if construction_type == CONSTANT_CONSTRUCTION:
		degree_function = get_constant_branch_and_leaf_factors
	elif construction_type == RANDOM_CONSTRUCTION:
		degree_function = get_randomized_branch_and_leaf_factors

	# Build a leafy tree
	leafy_tree = create_leafy_tree(number_of_nodes, degree_function)

	# Build a graph out of the tree
	hard_graph = graph_containing_tree(leafy_tree)

	return hard_graph


# Returns a tree with many leaves
def create_leafy_tree(number_of_nodes, get_branch_and_leaf_factors):

	# Create an empty graph
	tree = Graph(number_of_nodes)

	# Maintain a random-ordered list of unused nodes
	unused_nodes = [i for i in range(1, number_of_nodes)]
	shuffle(unused_nodes)

	# Maintain a queue of nodes not yet expanded
	nodes_to_expand = []

	# Start the tree at some node
	nodes_to_expand.append(unused_nodes.pop())

	# Expand the tree until it reaches all nodes
	while len(nodes_to_expand) > 0:
		current_node = nodes_to_expand.pop(0)





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

# Returns a list of all nodes in the tree that are leaves (degree one)
def get_leaves(tree):
	leaves = []
	for node in range(0, len(tree.neighbors)):
		if len(tree.neighbors[node]) == 1:
			leaves.append(node)

	return leaves


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



