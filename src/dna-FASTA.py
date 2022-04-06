'''
NAME: dna - FASTA
VERSION: 1
AUTOR: Diana Delgado Gutierrez
DESCRIPTION: Generar un archivo FASTA a partir de un archivo .txt existente en el directorio data.
USAGE: ejercicio
ARGUMENTS: string
SOFTWARE REQUIREMENTS: python 3.10
INPUT: archivo dna.txt
OUTPUT: archivo dns.fasta
'''
# Copiar el contenido de dna.txt
contenido = open("data/dna.txt")
contenidoDna = contenido.read()
dna = contenidoDna.rstrip("\n")
contenido.close()

# Crear el archivo FASTA y copiar el .txt
# Escribir la ubicación en la que queremos guardar el FASTA.
fastaArchivo = open("results/dna.fasta", "w")
fastaArchivo.write(">sequence_name \n" + dna)
fastaArchivo.close()
