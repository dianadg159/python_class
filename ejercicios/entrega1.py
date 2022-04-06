'''
NAME: Función input
VERSION: 1
AUTOR: Diana Delgado Gutierrez
DESCRIPTION: Dar una secuencia distinta con el mismo programa.
USAGE: ejercicio
ARGUMENTS: string
SOFTWARE REQUIREMENTS: python 3.10
INPUT: string
OUTPUT: string
'''
# Ejercicio 1 : Calcular la cantidad de A, T, C y G
# La secuencia de adn
print("Introduce una secuencia de adn para saber si cantidad de A, T, C y G: \n")
dna = input()
# La cantidad de A, T, C y G.
print(
    f"Porcentaje de AT: {porcentajeAT}% \n Porcentaje de CG: {porcentajeCG}%")

# Ejercicio 3 : Archivo fasta.
# Hacer el archivo fasta
fastaArchivo = open("dna.fasta", "w")
# Copiar el contenido de dna.txt
contenido = open("data/dna.txt")
contenidoDna = contenido.read()
dna2 = contenidoDna.rstrip("\n")
# Escribir en el archivo fasta
fastaArchivo.write(">sequence_name \n" + dna2)
# El output
