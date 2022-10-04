'''
NAME
 Handling fastq format
    
VERSION
    1.0

AUTOR
	Diana :)

DESCRIPTION
    Función que con un umbral determinado regresa los ids
    del archivo fastq que superen dicho umbral de calidad.

CATEGORY
    FASTQ

USAGE
    py .\src\formatFatsq.py

ARGUMENTS
    -u --umbral: número que determine el umbral de calidad.
    -f --file: path/to/file fastq

SOFTWARE REQUIREMENTS
Python 3.10

INPUT
    Umbral del usuario
    path/to/file fasta

OUTPUT
    ./data/qualityIds
'''
#! /usr/bin/env python3
# Importar librería
from Bio import SeqIO
import argparse

# input
parser = argparse.ArgumentParser(
    description="Script que regresa las secuencias de un fastq que superan un umbral.")

parser.add_argument("-f", "--file",
                    help="path/to/file de fastq",
                    required=True)
parser.add_argument("-u", "--umbral",
                    type=int,
                    help="umbral que tiene que superar",
                    required=True)

# Asignar variables
argumentos = parser.parse_args()

# función para el archivo de ids de calidad


def qualityRecords(archivo, umbral):
    '''
    Checa que todos los nucleótidos de la secuencia supere
    el umbral dado por el usuario.
        Parameters:
            archivo (str): Path del archivo fastq
            proporcionado por el usuario.
            umbral (int): Número que determina el umbral
            de calidad permitido por el usuario
        Returns:
            qlectures (int): Número de secuecias que pasan el umbral. 
    '''
    # Iniciar un contador
    qlectures = 0
    # ciclo para parsear las secuencias
    for record in SeqIO.parse(archivo, "fastq"):
        # acomodar de menor a mayor los Q values
        qscores = record.letter_annotations["phred_quality"]
        qscores.sort()
        if qscores[0] >= umbral:
            # contar las secuencias donde todos sus nt pasen el umbral
            qlectures += 1
            with open("results/qualityIds", "a") as ids:
                # escribir el id y la secuencia
                ids.write(record.id + "\n")
                ids.write(str(record.seq) + "\n")
                ids.write("\n")
                ids.close()
    return(str(qlectures))


noRecords = qualityRecords(argumentos.input, argumentos.umbral)
print("El número de secuencias que pasan el umbral: %s" % (noRecords))
print("Las secuencias están en el archivo results/qualiyId")
