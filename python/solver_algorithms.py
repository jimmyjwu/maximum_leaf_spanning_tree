from graph import *
from graph_helper import *
from constants import *

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


# YOUR CLEVER ALGORITHMS HERE


# Maintain a list of all (algorithm name, algorithm function) so that they can be
# systematically called from graph_solver.py
ALGORITHMS = [
	('example algorithm', example_algorithm),
	('example algorithm 2', example_algorithm_2)
]