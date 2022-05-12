'''# Include standard modules, la biblioteca
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version",
                    help="show program version", action="store_true")
# Si viene la opción en el pase de argumentos, le asigna True

# Read arguments from the command line
args = parser.parse_args()
print(args)

# Check for --version or -V
if args.version:  # Si la variable args en version es true.
    print("This is myprogram version 0.1")'''

import argparse
import os
import sys
# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',  # Nombre para las descripciones, así lo lee el programa
                       type=str,
                       help='the path to list')

# Execute the parse_args() method; leer argumentos
args = my_parser.parse_args()

input_path = args.Path  # no es necesaria la variable

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
print('\n'.join(os.listdir(input_path)))  # listar el contenido que pasamos.
