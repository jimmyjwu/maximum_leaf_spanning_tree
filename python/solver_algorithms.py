import util
from graph import *
from graph_helper import *
from constants import *
from disjointsets import *

"""
This file contains all the algorithms we have written to extract a leafy spanning tree
from a graph.

Every algorithm should be written in its own function, conforming to the following signature:

	def my_algorithm(graph):
		# Clever algorithm goes here
		return tree

IMPORTANT: At the bottom of this file, make sure that all algorithm functions are stored
in the ALGORITHMS list. This allows them to be called from graph_solver.py.
"""

def randomized_tree(graph):
	# Fill out graph attributes
	graph.search()
	nodes = get_nodes(graph)

	edges = get_edges(graph)
	most_leaves = 0
	best_tree = None

	# Run N iterations of randomized algorithm, save the best 
	for i in range(0, 10000):

		# Add all vertices of graph to disjoint set
		disjoint_set = UnionFind()
		disjoint_set.insert_objects(nodes)

		# Shuffle edges to make function stochastic
		shuffle(edges)

		num_edges = 0
		current_tree = Graph(graph.num_nodes)

		# Build graph
		for edge in edges:
			u, v = edge.ends

			# Add edge if it doesn't create a cycle
			if disjoint_set.find(u) != disjoint_set.find(v):
				disjoint_set.union(u, v)
				current_tree.add_edge(edge)
				num_edges += 1

			# Check leaves when tree is complete, |E| = |V| - 1
			if num_edges == graph.num_nodes - 1:
				num_leaves = get_leaves(current_tree)
				
				# Update best_tree if better num_leaves
				if num_leaves > most_leaves:
					most_leaves = num_leaves
					best_tree = current_tree

				break

	return best_tree


# Implements the Lu-Ravi algorithm in the paper "Approximating Maximum Leaf
# Spanning Trees in Almost Linear Time"
def joined_forest_tree(graph):

	def maximally_leafy_forest(graph):
		# Initialization
		G = create_copy(graph)
		E = get_edges(G)
		V = get_nodes(G)
		S = UnionFind()
		d = {}
		F = set()

		for v in V:
			S.find(v)
			d[v] = 0

		for v in V:
			S_prime = {}	# Maps vertex to union-find set index
			d_prime = 0
			for u in G.neighbors[v]:
				if S.find(u) != S.find(v) and S.find(u) not in S_prime.values():
					d_prime += 1
					S_prime[u] = S.find(u)
			if d[v] + d_prime >= 3:
				for u in S_prime:
					F.add(Edge(u,v))
					S.union(u, v)
					d[u] += 1
					d[v] += 1

		return F

	leafy_forest = maximally_leafy_forest(graph)

	unused_edges = get_edge_difference(graph, leafy_forest)
	leafy_spanning_tree = create_spanning_tree_from_forest(leafy_forest, unused_edges)

	return leafy_spanning_tree


# Takes a leafy forest (a Graph instance composed of one or more disjoint trees) and
# a list of unused edges in the original graph.
# Returns a leafy spanning tree of the original graph.
def create_spanning_tree_from_forest(forest, unused_edges):



	return


# YOUR CLEVER ALGORITHMS HERE


# Maintain a list of all (algorithm name, algorithm function) so that they can be
# systematically called from graph_solver.py
ALGORITHMS = [
	('Joined Forest Tree', joined_forest_tree)
]