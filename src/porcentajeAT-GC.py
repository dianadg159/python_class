'''
NAME: 
    Porcentaje de AT y GC
VERSION:
    1
AUTOR: 
    Diana Delgado Gutierrez
DESCRIPTION: 
    Programa que calcula el porcentaje de AT y GC con nombre y ruta del archivo input de secuencia.
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

# Pedir el nombre y ruta del archivo con la secuecia de DNA para leerlo.
print("¿Cuál es el nombre y ruta del archivo de DNA para calcular el porcentaje de AT y GC?")
archivoNombre = input()
secuencia = open(archivoNombre)
dna = secuencia.read()

# Calcular porcentaje
# Contar A+T entre el total de la secuencia por cien.
print(f"La secuencia es: {dna}")
porcentajeAT = (dna.count('A') + dna.count('T')) / len(dna) * 100
porcentajeCG = (dna.count('C') + dna.count('G')) / len(dna) * 100
print(f"Archivo de la secuencia: {archivoNombre}")
print(
    f"Porcentaje de AT: {porcentajeAT}% \n Porcentaje de CG: {porcentajeCG}%")

# Cerrar archivo
secuencia.close()
