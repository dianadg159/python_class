'''
NAME
    Regiones ricas en AT

VERSION
    1.0
    
AUTOR
	Diana Delgado Gutiérrez
 
DESCRIPTION
    Recibe como argumento el archivo de secuencia de DNA
    y el tamaño mínimo de la región rica en AT's
    a buscar.
    
CATEGORY
    DNA
    
USAGE
    
    
ARGUMENTS
    -f archivo con secuencia de ADN a leer.
    -s [número] tamaño de la región rica en AT.
    
SOFTWARE REQUIREMENTS
    Python 3.10
    
INPUT
    Archivo con una secuencia de ADN.
    Longitud en bases de la region mínima de AT.
    
OUTPUT
    Posición de las regigones ricas en AT.
'''
# Importando librerías.
import re
import argparse

# Input
parser = argparse.ArgumentParser(
    description="Script que detecta regiones ricas en AT.")
parser.add_argument("-f", "--file",
                    help="Atchivo con la secuencia de ADN.",
                    required=True)
parser.add_argument("-s", "--size",
                    help="Longitud de la región con AT.",
                    required=False)

# Asignar variables al input.
argumentos = parser.parse_args()
file = argumentos.file
size = argumentos.size

# Abrir el archivo y leerlo.
dna = open(file, "r")
seqdna = dna.read().upper()

# Checar que la secuencia sea ADN


def revise(seqdna):
    errores = re.finditer("[^ATGC]+", seqdna)
    if (errores):
        # Imprimir los errores.
        for error in errores:
            print("Se encuentran errores en: " + str(error.span()))
        return(1)
    else:
        return(0)


# Encontrar las regiones ricas en AT del tamaño size.
def rich_at_regions(seqdna, size=13):
    at_rich = re.finditer("(A+|T+){" + size + ",}", seqdna, re.IGNORECASE)
    matches = len(
        [*re.finditer("(A+|T+){" + size + ",}", seqdna, re.IGNORECASE)])
    if matches:
        for region in at_rich:
            at_seq = region.group()
            print(
                f"Se encuentra la región {at_seq} en la posición: {region.span()}")
    else:
        print(f"No hubo region de AT de {size}")


# Llamar funciones.
revise(seqdna)
rich_at_regions(seqdna, size)
