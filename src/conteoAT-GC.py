'''
NAME: 
    Conteo de A,C,G y T
VERSION: 
    1.1
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
print(
    f"El total por base es: \n A:{dna.count('A')} T:{dna.count('T')}  C:{dna.count('C')}  G:{dna.count('G')}")
