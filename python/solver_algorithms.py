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

	# Bests so far
	most_leaves = 0
	best_tree = None

	# Run N iterations of randomized algorithm, save the best 
	for i in range(0, NUMBER_OF_RANDOM_RUNS):

		# Add all vertices of graph to disjoint set
		disjoint_set = UnionFind()
		disjoint_set.insert_objects(nodes)

		# Shuffle edges to make function stochastic
		shuffle(edges)

		num_edges = 0
		current_tree = Graph(MAXIMUM_NUMBER_OF_NODES)

		# Build graph
		for edge in edges:
			u, v = edge.ends

			# Add edge if it doesn't create a cycle
			if disjoint_set.find(u) != disjoint_set.find(v):
				disjoint_set.union(u, v)
				current_tree.add_edge(edge)
				num_edges += 1

			# Check leaves when tree is complete, |E| = |V| - 1
			if num_edges == len(nodes) - 1:
				num_leaves = len(get_leaves(current_tree))
				
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

		return make_graph(F)

	# Takes a leafy forest (a Graph instance composed of one or more disjoint trees) and
	# a list of unused edges in the original graph.
	# Returns a leafy spanning tree of the original graph.
	def create_spanning_tree_from_forest(forest, unused_edges):

		def is_leaf(node):
			return len(forest.neighbors[node]) == 1

		spanning_tree = create_copy(forest)

		nodes = get_nodes(forest)
		edges = get_edges(forest)

		# Initialize meta-graph
		connected_components = UnionFind()
		connected_components.insert_objects(nodes)
		for edge in edges:
			connected_components.union(edge.ends[0], edge.ends[1])

		# Sort unused edges by tier as follows:
		# 1. Edge from internal node to internal node
		# 2. Edge from internal node to leaf
		# 3. Edge from leaf to leaf
		internal_to_internal_edges = []
		internal_to_leaf_edges = []
		leaf_to_leaf_edges = []
		for edge in unused_edges:
			u, v = edge.ends
			if not is_leaf(u) and not is_leaf(v):
				internal_to_internal_edges.append(edge)
			elif is_leaf(u) and is_leaf(v):
				leaf_to_leaf_edges.append(edge)
			else:
				internal_to_leaf_edges.append(edge)
		unused_edges = internal_to_internal_edges
		unused_edges.extend(internal_to_leaf_edges)
		unused_edges.extend(leaf_to_leaf_edges)

		# Add edges (by tier) if it doesn't induce a cycle
		for edge in unused_edges:
			u, v = edge.ends
			if connected_components.find(u) != connected_components.find(v):
				spanning_tree.add_edge(edge)
				connected_components.union(u, v)

		return spanning_tree

	leafy_forest = maximally_leafy_forest(graph)

	unused_edges = get_edge_difference(graph, leafy_forest)
	leafy_spanning_tree = create_spanning_tree_from_forest(leafy_forest, unused_edges)

	return leafy_spanning_tree


# YOUR CLEVER ALGORITHMS HERE




# Maintain a list of all (algorithm name, algorithm function) so that they can be
# systematically called from graph_solver.py
ALGORITHMS = [
	('joined forest tree', joined_forest_tree),
	('randomized tree', randomized_tree)
]


