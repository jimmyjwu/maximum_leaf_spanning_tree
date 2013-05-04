from graph import *
from graph_helper import *
from constants import *
from input_output import *
from solver_algorithms import *

"""
This file extracts leafy spanning trees from graphs, for part 2 of the MLST project.
"""

# Takes a list of graphs and returns the leafiest spanning tree we can find
# by running them through all of our algorithms
def find_leafy_spanning_trees(graphs):
	leafy_spanning_trees = []

	for graph in graphs:
		best_tree = find_leafy_spanning_tree(graph)
		leafy_spanning_trees.append(best_tree)

	return leafy_spanning_trees




# Takes a graph and returns the leafiest spanning tree we can find by running
# it through all of our algorithms
def find_leafy_spanning_tree(graph):

	# Maintain a record of bests so far
	best_tree = None
	best_leaf_count = 0
	best_algorithm = ''

	# Try all algorithms and record the best one
	for algorithm_name, algorithm in ALGORITHMS:
		tree = algorithm(graph)
		tree.search()

		if tree.num_leaves > best_leaf_count:
			best_tree = tree
			best_leaf_count = tree.num_leaves
			best_algorithm = algorithm_name

	# Log the best solution
	print('Best tree found with ' + best_leaf_count + ' leaves using ' + algorithm_name + ' algorithm.')

	return best_tree




