from graph import *
from constants import *
from random import shuffle
import networkx as nx
# import matplotlib.pyplot as plt

"""
This file contains convenient helper methods for graphs.
"""

# Returns whether the two given graph are equivalent (contain same edges and nodes)
def are_equivalent_graphs(graph_1, graph_2):

	# Test for same node sets
	nodes_1 = set(get_nodes(graph_1))
	nodes_2 = set(get_nodes(graph_2))
	if nodes_1 != nodes_2:
		return False

	# Test for same edge sets
	edges_1 = set(get_edges(graph_1))
	edges_2 = set(get_edges(graph_2))
	if edges_1 != edges_2:
		return False

	return True

# Returns whether the first given graph is a subgraph of the second
def is_subgraph(graph_1, graph_2):
	edges_1 = set(get_edges(graph_1))
	edges_2 = set(get_edges(graph_2))

	return edges_1 <= edges_2


# Returns a list of nodes in the graph
def get_nodes(graph):
	nodes = set()
	edges = get_edges(graph)

	for edge in edges:
		nodes.add(edge.ends[0])
		nodes.add(edge.ends[1])

	return list(nodes)


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
	number_of_nodes = len(get_nodes(graph))
	unused_edge_set = set()

	for current_node in range(0, number_of_nodes):
		current_node_neighbors = set(graph.neighbors[current_node])
		for other_node in range(0, number_of_nodes):
			if current_node != other_node:
				if other_node not in current_node_neighbors:
					unused_edge_set.add(Edge(current_node, other_node))

	return list(unused_edge_set)


# Returns a list of edges in the graph but not in its subgraph
def get_edge_difference(graph, subgraph):
	graph_edges = get_edges(graph)
	subgraph_edges = set(get_edges(subgraph))
	edge_difference = []

	for edge in graph_edges:
		if edge not in subgraph_edges:
			edge_difference.append(edge)

	return edge_difference


# Returns a list of all nodes in the tree that are leaves (degree one)
def get_leaves(tree):
	leaves = []
	for node in range(0, len(tree.neighbors)):
		if len(tree.neighbors[node]) == 1:
			leaves.append(node)

	return leaves


# Returns a deep copy of the given graph
def create_copy(graph):
	edges = get_edges(graph)
	return make_graph(edges)


# Returns whether the given graph is a tree
def is_tree(graph):
	number_of_nodes = len(get_nodes(graph))
	number_of_edges = len(get_edges(graph))
	return number_of_edges == number_of_nodes - 1


# Returns whether the given graph is a line
def is_line(graph):
	# If not a tree, no chance it's a line
	if not is_tree(graph):
		return False

	# Graph is a line iff it is a tree with two nodes having degree 1 and all
	# others having degree 2
	nodes = get_nodes(graph)
	leaf_count = 0
	for node in nodes:
		degree = len(graph.neighbors[node])
		if degree == 1:
			leaf_count += 1
			if leaf_count > 2:
				return False
		elif degree != 2:
			return False

	# Passed tests; graph is a line
	return True


# Plots a graph
def plot_graph(graph):
	G = nx.Graph()
	G.add_nodes_from(get_nodes(graph))
	for edge in get_edges(graph):
		G.add_edge(edge.ends[0], edge.ends[1])
	nx.draw(G)
	plt.show()


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


