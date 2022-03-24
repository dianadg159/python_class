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
print(f"La secuencia \n {dna} \n tiene {dna.count('A')} adeninas, {dna.count('T')} timinas, {dna.count('C')} citocinas y {dna.count('G')} guaninas. ")

# Ejercicio 2 : porcentaje de A:T y G:C
# Pedir datos.
print("¿Cuál es el nombre y ruta del archivo de DNA para calcular el porcentaje de AT y GC?")
secuenciaArchivo = input()
# Leer el archivo
secuencia = open(secuenciaArchivo)
secuenciaContenido = secuencia.read()
dna = secuenciaContenido.rstrip("\n")
# Calcular porcentaje
print(f"La secuencia es: {dna}")
porcentajeAT = (dna.count('A') + dna.count('T')) / len(dna) * 100
porcentajeCG = (dna.count('C') + dna.count('G')) / len(dna) * 100
print(f"Archivo de la secuencia: {secuenciaArchivo}")
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
