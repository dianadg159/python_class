'''
NAME
    Conteo de péptidos
    
VERSION
    1.1

AUTOR
    Diana Delgado

DESCRIPTION
    Conteo de una cadena de aminoacidos

CATEGORY
    Ejercicio

ARGUMENTS
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                        Secuencia de aminoácidos a calcular
    -a AMINOACIDO, --aminoacido AMINOACIDO
                        El aminoacido que etsamos buscando

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    Secuencia de un péptido con el aminoacido que busca.

OUTPUT
    Porcentaje del aminoácido en la secuencia.
'''
import os
import argparse

# input: secuencia protéica y aa
parser = argparse.ArgumentParser(
    description="Script que calcula la cantidad de un aminoácido en una secuencia.")

parser.add_argument("-i", "--input",
                    help="Secuencia de aminoácidos a calcular",
                    required=True)
parser.add_argument("-a", "--aminoacido",
                    help="El aminoacido que etsamos buscando",
                    required=True)

# Pedir los datos
argumentos = parser.parse_args()

# asignar variables
peptido = argumentos.input
aa = argumentos.aminoacido

# Calcular el porcentaje de un aa


def get_aa_percentage(peptido, aa):
    '''
    Regresa el porcentaje del aminoácido que introdujo el
    usuario en una seciancia peptídica.

        Parámetros:
            peptido (string): una secuencia de aminoácidos.
            aa (string): El aminoácido a buscar su porcentaje

        Returns:
            aa_percentage (float): porcentaje de aminoácido que hay
                                    en la secuencia.
    '''
    peptido = peptido.upper()
    aa = aa.upper()
    length = len(peptido)
    aa_count = peptido.count(aa)
    aa_percentage = aa_count / length * 100
    return aa_percentage


# output: porcentaje de aminoácido en la secuencia
print(
    f"El porcentaje de {aa} es: {get_aa_percentage(peptido, aa)}%")
