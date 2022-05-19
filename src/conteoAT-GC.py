'''
NAME:
    Conteo de A,C,G y T
VERSION:
    2
AUTOR:
    Diana Delgado Gutierrez
DESCRIPTION:
    Programa que cuente el total de A,C,G y T que hay en una secuencia de DNA introducida por el usuario.
USAGE:
    ejercicio
ARGUMENTS:
    string
SOFTWARE REQUIREMENTS:
    python 3.10
INPUT:
    string
OUTPUT:
    string
'''

# Pedir la secuencia de DNA al usuario.
print("Introduce una secuencia de adn para saber si cantidad de A, T, C y G: \n")
dna = input().upper()

# Generar un ValueError cuando no se da una secuencia de ADN.
if (dna.count('A') == 0 & dna.count('T') == 0 & dna.count('C') == 0 & dna.count('G') == 0):
    raise ValueError('Lo que introduciste no es una secuencia de ADN.')

# La cantidad de A, T, C y G.


def get_AT_content(dna, decimales):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return str(round(at_content, decimales))


def get_GC_content(dna, decimales):
    length = len(dna)
    g_count = dna.upper().count('G')
    c_count = dna.upper().count('C')
    gc_content = (c_count + g_count) / length
    return str(round(gc_content, decimales))


print("Contenido de AT: " + get_AT_content(dna, 2))
print("Contenido de GC: " + get_GC_content(dna, 2))
