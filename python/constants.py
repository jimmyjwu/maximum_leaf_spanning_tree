"""
Define all constants in this file.
"""

# Parameters for choosing which degree function to use in tree construction
CONSTANT = 1234
RANDOM = 2345

# Parameters for randomized branch and leaf factors
MINIMUM_DEGREE = 2
MAXIMUM_DEGREE = 10

# Parameters for constant branch and leaf factors
BRANCH_FACTOR = 4
LEAF_FACTOR = 5

# General parameters for graph generation
MAXIMUM_NUMBER_OF_NODES = 100
MAXIMUM_NUMBER_OF_EDGES = 2000

# File names
OUR_GRAPHS = 'hard.in'
OUR_TREES = 'hard.out'
ALL_GRAPHS_INPUT = 'hard.all.v3.in'
ALL_TREES_OUTPUT = 'hard.all.v3.out'
TEMPORARY_TREES_OUTPUT = 'hard.all.v3.out_temporary'
MANUALLY_SOLVED_GRAPHS = 'manually_solved.in'
MANUALLY_SOLVED_TREES = 'manually_solved.out'

# Spanning tree algorithm parameters
NUMBER_OF_RANDOM_RUNS = 100

# Parameter to decide which graphs are small enough to be manually solved
SMALL_NUMBER_OF_EDGES = 25