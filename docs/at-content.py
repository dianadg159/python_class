import argparse

parser = argparse.ArgumentParser(
    description="Script que calcula la cantidad de AT en una secuencia.")

parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

parser.add_argument("-o", "--output",
                    help="Path for the output file",
                    required=False)

parser.add_argument("-r", "--round",
                    help="number of digits to rouond",
                    type=int,
                    required=False)

with open(parser.input, "r") as seq:
    my_dna = seq.read

porcentajeAT = (my_dna.count('A') + my_dna.count('T')) / len(my_dna) * 100
print(porcentajeAT)
