from graph import *
from graph_helper import *
from constants import *

# Outputs several graphs to a text file in the format given by instructors
def output_graphs_to_new_file(graphs, file_name):
	output_file = open(file_name, 'w')

	number_of_graphs = len(graphs)
	output_file.write(str(number_of_graphs) + '\n')

	for graph in graphs:
		output_graph_to_existing_file(graph, output_file)

	output_file.close()


# Outputs the graph to a text file in the format given by instructors
def output_graph_to_existing_file(graph, output_file):

	# Build a list of distinct edges
	edges = get_edges(graph)

	# Output number of edges in this graph to file
	number_of_edges = len(edges)
	output_file.write(str(number_of_edges) + '\n')

	# Output all the edges in this graph to file
	for edge in edges:
		u = edge.ends[0]
		v = edge.ends[1]
		output_file.write(str(u) + ' ' + str(v) + '\n')