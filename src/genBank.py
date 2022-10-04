'''
NAME
 Handling GenBank archive

VERSION
    1.0

AUTOR
	Diana :)

DESCRIPTION
    Programa que imprime características del organismo y genes
    del mismo con un archivo GenBank.

CATEGORY
    GenBank

USAGE
    py .\src\genBank.py

ARGUMENTS
    -g --genes: numero de gen que quiere el usuario.
    -f --file: path/to/file genbank

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    Umbral del usuario
    path/to/file fasta

OUTPUT
    en pantalla:
        Organismo: 
        Fecha: 
        Country: 
        Isolate: 
        [geneID/prot/ID]
        DNA: 
        RNA: 
        Prot: 
'''
#! /usr/bin/env python3
# Importar librería
from Bio import SeqIO
import argparse

# input
parser = argparse.ArgumentParser(
    description="Script que regresa features y genes del archivo virus.gb.")

parser.add_argument("-f", "--file",
                    help="path/to/file de genebank",
                    required=True)
parser.add_argument("-g", "--genes",
                    type=int,
                    help="numero de gen que quiere la secuencia (1:11)",
                    required=True)

# Asignar variables
argumentos = parser.parse_args()

# Función para sacar genes del archivo


def resumen(archivo, genes):
    '''
    Script que regresa features y genes de un archivo genbank.
        Parameters:
            archivo (str): Path del archivo genbank
            proporcionado por el usuario.
            genes (int): Número de gen deseado por el usuario.
        Returns:
            none. 
    '''
    # Abrir archivo
    for gb_record in SeqIO.parse(archivo, "genbank"):
        # Anotaciones
        print(f"Organismo: {gb_record.annotations['organism']}")
        print(f"Fecha: {gb_record.annotations['date']}")
        # Features
        country = gb_record.features[0].qualifiers['country']
        print(f"Country: {country[0]}")
        isolate = gb_record.features[0].qualifiers['isolation_source']
        print(f"Isolate: {isolate[0]}")
        # Genes
        gene_id = gb_record.features[genes].qualifiers['db_xref']
        print(gene_id[0])
        # Secuencias
        start = gb_record.features[genes].location.nofuzzy_start
        #end = gb_record.features[2].location.nofuzzy_end
        gene_seq = gb_record.seq[start:start + 15]
        print(f"DNA: {gene_seq}")
        print(f"RNA: {gene_seq.complement()}")
        print(f"Prot: {gene_seq.translate()}")


resumen(argumentos.file, argumentos.genes)
