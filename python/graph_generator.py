from graph import *

# Create graph with 100 nodes



# Populate the graph with up to 2000 edges
# Choose edges such that there exists a leafy tree within, but hard to find


# Returns a hard graph instance
def create_hard_graph():
	leafy_tree = create_leafy_tree(100)
	hard_graph = graph_containing_tree(leafy_tree)

	return hard_graph


# Returns a tree with many leaves
def create_leafy_tree(number_of_nodes):
	tree = Graph(100)

	# Populate the tree with appropriate edges



	return tree



# Takes a tree and returns a general graph that contains the tree and obscures its leaves.
def graph_containing_tree(tree):
	# Add edges to tree so as to make its leaves hard to find



	return tree




# Outputs the graph to a text file in the format given by instructors
def output_graph_to_text_file(graph):
