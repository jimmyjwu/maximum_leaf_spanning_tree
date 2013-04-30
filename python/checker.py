import config
import reader

import sys

def print_error(err):
    sys.stderr.write(err)

def print_message(msg):
    sys.stdout.write(msg)

def check_input():
    infile = config.DEFAULT_INPUT_FILE if len(sys.argv) <= 1 else sys.argv[1]

    edge_sets = None
    try:
        f = open(infile)
        in_reader = reader.InFileReader(f)
        edge_sets = in_reader.read_input_file()
        print_message("Input file '{0}' has the correct format.\n".format(infile))

    except IOError as e:
        print_error("Error reading '{0}' ({1}).\n".format(infile, e))
    except reader.ReaderException as e:
        print_error("({0}) {1}\n".format(infile, e))

    return edge_sets

def check_output(check_output_program_name):
    num_args = len(sys.argv)-1

    if num_args == 0:
        outfile = config.DEFAULT_OUTPUT_FILE
    elif num_args == 2:
        outfile = sys.argv[2]
    else:
        print_error((
            "usage: {0} [file.in file.out]\n\n"+
            "  Check the format of \"file.out\" against \"file.in\".\n"+
            "Error: Must provide either two arguments, or zero "+
            "arguments to use the default\n"+
            "input \"{1}\" and output \"{2}\". (Number of arguments "+
            "is {3})\n").format(check_output_program_name,
                config.DEFAULT_INPUT_FILE, config.DEFAULT_OUTPUT_FILE,
                num_args))
        return None

    edge_sets = check_input()
    num_leaves = None
    if not edge_sets:
        return None

    try:
        f = open(outfile)
        out_reader = reader.OutFileReader(f)
        num_leaves = out_reader.read_output_file(edge_sets)
        print_message("Output file '{0}' has the correct format.\n".format(outfile))
        for i in range(len(edge_sets)):
            print_message("Output tree {0} has {1} leaves.\n".format(i+1, num_leaves[i]))

    except IOError as e:
        print_error("Error reading '{0}' ({1}).\n".format(outfile, e))
    except reader.ReaderException as e:
        print_error("({0}) {1}\n".format(outfile, e))

    return num_leaves
