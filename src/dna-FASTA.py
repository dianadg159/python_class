'''
NAME: 
  dna-FASTA
  
VERSION:
  2
  
AUTOR: 
  Diana Delgado Gutierrez
  
DESCRIPTION: 
  Generar un archivo FASTA a partir de un archivo .txt existente en el directorio data.
  
USAGE: 
  dna-FASTA.py [-h] -i INPUT -o OUTPUT [-n NAME]
  
ARGUMENTS:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path del archivo con secuencia de adn     
  -o OUTPUT, --output OUTPUT
                        Path del archivo en formato fasta
  -n NAME, --name NAME  Nombre que poner a la secuencia
  
SOFTWARE REQUIREMENTS:
  python 3.10
  
INPUT: 
  data/archivo.txt
  
OUTPUT:
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
parser.add_argument("-n", "--name",
                    help="Nombre que poner a la secuencia",
                    required=False)

# Pedir los datos
argumentos = parser.parse_args()

# Copiar el contenido del archivo del usuario
input = argumentos.input
contenido = open(input)
contenidoDna = contenido.read()
dna = contenidoDna.rstrip("\n")
contenido.close()

# Crear el archivo FASTA y copiar el .txt
# Escribir la ubicación en la que queremos guardar el FASTA.


def archivoFasta(argumentos):
    output = argumentos.output
    fastaArchivo = open(output, "w")
    if argumentos.name:
        fastaArchivo.write(">" + argumentos.name + "\n" + dna)
    else:
        fastaArchivo.write(">sequence_name \n" + dna)
    fastaArchivo.close()


archivoFasta(argumentos)
