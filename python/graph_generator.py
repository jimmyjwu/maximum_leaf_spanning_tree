from graph import *
from constants import *
from input_output import *
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


# Returns a tree and its corresponding hard graph
# construction_type specifies which node-expansion function to use when building tree
def create_hard_tree_and_graph(construction_type):

	# Define the degree function for constant tree construction
	def get_constant_branch_and_leaf_factors():
		return BRANCH_FACTOR, LEAF_FACTOR

	# Define the degree function for randomized tree construction
	def get_randomized_branch_and_leaf_factors():
		degree = randint(MINIMUM_DEGREE, MAXIMUM_DEGREE)
		random_factor = randint(1, degree - 1)
		leaf_factor = max(random_factor, degree - random_factor)
		branch_factor = degree - leaf_factor
		return branch_factor, leaf_factor

	# Select the correct degree function
	degree_function = None
	if construction_type == CONSTANT:
		degree_function = get_constant_branch_and_leaf_factors
	elif construction_type == RANDOM:
		degree_function = get_randomized_branch_and_leaf_factors

	# Build a leafy tree
	leafy_tree = create_leafy_tree(MAXIMUM_NUMBER_OF_NODES, degree_function)

	# Build a graph out of the tree
	hard_graph = graph_containing_tree(leafy_tree)

	return leafy_tree, hard_graph


# Returns a tree with many leaves
def create_leafy_tree(number_of_nodes, get_branch_and_leaf_factors):

	# Create an empty graph
	tree = Graph(number_of_nodes)

	# Maintain a random-ordered list of unused nodes
	unused_nodes = [i for i in range(0, number_of_nodes)]
	shuffle(unused_nodes)

	# Maintain a queue of nodes not yet expanded
	nodes_to_expand = []

	# Start the tree at some node
	nodes_to_expand.append(unused_nodes.pop())

	# Expand the tree until it reaches all nodes
	while len(nodes_to_expand) > 0:
		current_node = nodes_to_expand.pop(0)

		# Determine the expansion rules for this node
		branch_factor, leaf_factor = get_branch_and_leaf_factors()

		while leaf_factor > 0 and len(unused_nodes) > 0:
			new_leaf = unused_nodes.pop()
			tree.add_edge(Edge(current_node, new_leaf))
			leaf_factor -= 1

		while branch_factor > 0 and len(unused_nodes) > 0:
			new_branch = unused_nodes.pop()
			tree.add_edge(Edge(current_node, new_branch))
			nodes_to_expand.append(new_branch)
			branch_factor -= 1

	return tree



# Takes a tree and returns a general graph that contains the tree and obscures its leaves.
def graph_containing_tree(tree):

	# Create a working copy of the tree (so we don't modify original)
	tree_edges = get_edges(tree)
	graph = make_graph(tree_edges)

	# Add random edges to tree to obscure its leaves
	leaves = get_leaves(graph)

	# Maintain a hash that stores, for each leaf in the original tree, how many more edges
	# can be added to it before its degree equals its parent's
	degree_remaining = {}
	for leaf in leaves:
		parent = graph.neighbors[leaf][0]
		degree_remaining[leaf] = len(graph.neighbors[parent]) - 1

	# Maintain a random-sorted list of all possible edges between edges
	unused_leaf_edges = set()
	for leaf_1 in leaves:
		for leaf_2 in leaves:
			if leaf_1 != leaf_2:
				unused_leaf_edges.add(Edge(leaf_1, leaf_2))
	unused_leaf_edges = list(unused_leaf_edges)
	shuffle(unused_leaf_edges)

	# Add random edges between leaves until graph has maximum allowed number of
	# edges, or each original leaf has reached the degree of its parent
	remaining_number_of_edges = MAXIMUM_NUMBER_OF_EDGES - len(get_edges(graph))
	while remaining_number_of_edges > 0 and len(unused_leaf_edges) > 0:
			edge = unused_leaf_edges.pop()
			if degree_remaining[edge.ends[0]] > 0 and degree_remaining[edge.ends[1]] > 0:
				graph.add_edge(edge)
				remaining_number_of_edges -= 1
				degree_remaining[edge.ends[0]] -= 1
				degree_remaining[edge.ends[1]] -= 1

	return graph


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

