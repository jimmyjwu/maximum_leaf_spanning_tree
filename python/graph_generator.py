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



	# Populate the tree with appropriate edges
	build_leafy_tree(0, number_of_nodes)


	return tree



# Takes a tree and returns a general graph that contains the tree and obscures its leaves.
def graph_containing_tree(tree):

	# Maintain a random-ordered list of unused edges
	unused_edges = find_unused_edges(tree)
	shuffle(unused_edges)

	# Add random edges to tree to obscure its leaves


	return tree

# Returns a list of edges not used in the graph.
def find_unused_edges(graph):
	unused_edges = []


	return unused_edges



# Outputs the graph to a text file in the format given by instructors
def output_graph_to_text_file(graph):
