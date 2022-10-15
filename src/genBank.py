'''
NAME
 Handling GenBank archive

VERSION
    2.0

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
    -g --genes: Nombre de gen que quiere el usuario.
    -f --file: path/to/file genbank (./data/virus.gb)

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    Umbral del usuario
    path/to/file genbank (./data/virus.gb)

OUTPUT
    en pantalla:
        Organismo: 
        Fecha: 
        Country: 
        Isolate: 
        Gen:
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
                    nargs='*',
                    help="Nombre(s) de(l) gen(es) del que quiere la secuencia (G, L, M, P, N, L)",
                    required=True)

# Asignar variables
argumentos = parser.parse_args()

# Función para sacar genes del archivo


def resumen(archivo, genes):
    '''
    Regresa features y genes de un archivo genbank en 
    standard output.
        Parameters:
            archivo (str): Path del archivo genbank
            proporcionado por el usuario.
            genes (list): Nombres de genes deseados por el usuario.
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
        for gen in genes:
            # Obtener los features
            for i in gb_record.features:
                # Obtener los genes
                if i.type == "gene":
                    # Buscar los genes que pide el usuario
                    if i.qualifiers["gene"] == list(gen):
                        # Obtener su inicio de secuencia
                        start = i.location.nofuzzy_start
                        break
                    else:
                        # Si no existe el gen marcar la variable
                        start = 0
            if not(start):
                # Imprimir error
                print("No existe gen con el nombre " + gen)
                # Continuar con el siguiente gen
                continue
            # Imprimir datos del gen
            print("Gen: " + gen)
            #start = gb_record.features[genes].location.nofuzzy_start
            #end = gb_record.features[2].location.nofuzzy_end
            gene_seq = gb_record.seq[start:start + 15]
            print(f"DNA: {gene_seq}")
            print(f"RNA: {gene_seq.complement()}")
            print(f"Prot: {gene_seq.translate()}")


# LLamar la funcion
resumen(argumentos.file, argumentos.genes)
