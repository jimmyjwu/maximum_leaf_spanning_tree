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


def example_algorithm(graph):
	return Graph(MAXIMUM_NUMBER_OF_NODES)

def example_algorithm_2(graph):
	return Graph(MAXIMUM_NUMBER_OF_NODES)

def randomized_tree(graph):
	#Fill out graph attributes
	graph.search()
	nodes = get_nodes(graph)

	edges = get_edges(graph)
	most_leaves = 0
	best_tree = None

	# counter = util.Counter()
	#Run N-iterations of randomized algorithm, save the best 
	for i in range(0, 10000):
		#Add all vertices of graph to disjoint set
		disjoint_set = UnionFind()
		disjoint_set.insert_objects(nodes)

		#Shuffle edges to make function stochastic
		shuffle(edges)

		num_edges = 0
		current_tree = Graph(graph.num_nodes)

		#Build graph
		for edge in edges:
			u, v = edge.ends

			#Add edge if it doesn't create a cycle
			if disjoint_set.find(u) != disjoint_set.find(v):
				disjoint_set.union(u, v)
				current_tree.add_edge(edge)
				num_edges += 1

			#Check leaves when tree is complete, |E| = |V| - 1
			if num_edges == graph.num_nodes - 1:
				num_leaves = get_leaves(current_tree)
				# counter[len(num_leaves)] += 1
				#Update best_tree if better num_leaves
				if num_leaves > most_leaves:
					most_leaves = num_leaves
					best_tree = current_tree
				break

	# for i in range(0, graph.num_nodes):
	# 	print counter[i]

	return best_tree

# Implements the Lu-Ravi algorithm in the paper "Approximating Maximum Leaf
# Spanning Trees in Almost Linear Time"
def joined_forest_tree(graph):

	




	return maximally_leafy_forest(graph)	# Temporarily return the leafy forest

def maximally_leafy_forest(graph):
	# Initialization
	G = create_copy(graph)
	E = get_edges(G)
	V = get_nodes(G)
	S = {}		# S maps a node to a set of nodes
	d = {}		# d maps a node to a number 
	F = set()

	for v in V:
		S[v] = set([v])
		d[v] = 0

	for v in V:
		S_prime = {}		# S_prime maps a node to a set of nodes
		d_prime = 0

		for u in G.neighbors[v]:
			if u not in S[v] and S[u] not in S_prime.values():
				d_prime += 1
				S_prime[u] = S[u]

		if d[v] + d_prime >= 3:
			for u in S_prime:
				F.add(Edge(u,v))
				S[v] = S[v].union(S[u])
				S[u] = S[v].union(S[u])
				d[u] = d[u] + 1
				d[v] = d[v] + 1

	print(d)

	return F

# YOUR CLEVER ALGORITHMS HERE


# Maintain a list of all (algorithm name, algorithm function) so that they can be
# systematically called from graph_solver.py
ALGORITHMS = [
	('example algorithm', example_algorithm),
	('example algorithm 2', example_algorithm_2)
]