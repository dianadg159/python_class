'''
NAME
    Conteo de péptidos
    
VERSION
    1.0

AUTOR
    Diana Delgado

DESCRIPTION
    Conteo de una cadena de aminoacidos

CATEGORY
    Ejercicio

ARGUMENTS
    

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
peptido = argumentos.input.upper()
aa = argumentos.aminoacido.upper()

# Calcular el porcentaje de un aa


def get_aa_percentage(peptido, aa):
    length = len(peptido)
    aa_count = peptido.count(aa)
    aa_percentage = aa_count / length * 100
    return aa_percentage


# output: porcentaje de aminoácido en la secuencia
print(
    f"El porcentaje de {aa} es: {get_aa_percentage(peptido, aa)}%")

# Pruebas
try:
    assert get_aa_percentage(peptido="MSRSLLLRFLLFLLLLPPLP", aa="r") == 10.0
    assert get_aa_percentage(peptido="msrslllrfllfllllpplp", aa="L") == 50.0
except AssertionError as ex:
    print("Hubo un error de mayúsculas/minúsculas: " + ex.strerror)
else:
    assert get_aa_percentage(
        peptido="MSRSLLLRFLLFLLLLPPLP", aa="Y") == 0.0, "No está el aa que busca."
finally:
    assert get_aa_percentage(
        peptido="MSRSLLLRFLLFLLLLPPLP", aa="M") == 5.0, "No calcula bien el porcentaje :("
