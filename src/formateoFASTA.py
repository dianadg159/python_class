'''
NAME
    Formatear secuencia a Fasta
    
VERSION
    1.2

AUTOR
    Diana Delgado Gutiérrez 

DESCRIPTION
    Dado un archivo dna_sequences.txt de secuencias
    convertirlas a formato FastA en otro archivo output
    dna_sequences.FASTA

CATEGORY
    FASTA format

USAGE
    py src/formatoFASTA.py [-h] -i INPUT -o OUTPUT

ARGUMENTS
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                        Path del archivo con secuencia de adn
    -o OUTPUT, --output OUTPUT
                        Path del archivo en formato fasta

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    data/archivo.txt

OUTPUT
    results/archivo.fasta
'''
import argparse

# Pedir datos
parser = argparse.ArgumentParser(
    description="Script que pasa un archivo de secuancia adn a formato fasta.")

parser.add_argument("-i", "--input",
                    help="Path del archivo con secuencia de adn",
                    required=True)
parser.add_argument("-o", "--output",
                    help="Path del archivo en formato fasta",
                    required=True)

# Pedir los datos
args = parser.parse_args()

# Abrir archivo y leer cada línea.
contenido = open(args.input, "r")
secSinFormato = contenido.readlines()

# Cerrar el archivo.
contenido.close()

# Crear archivo output .FASTA
archivoOutput = open(args.output, "w")

# Editar cada secuencia a formato FASTA y escribir en archivo output.
for sec in secSinFormato:
    secLista = sec.split("   ")
    secId = secLista[0]
    secuencia = secLista[1]
    archivoOutput.write(f"> {str(secId)}\n")
    archivoOutput.write(str(secuencia.upper().replace("-", "")))

# Cerrar archivo FASTA.
archivoOutput.close()
