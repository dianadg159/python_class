'''
NAME
    Formatear secuencia a Fasta
    
VERSION
    1.1

AUTOR
    Diana Delgado Gutiérrez 

DESCRIPTION
    Dado un archivo dna_sequences.txt de secuencias
    convertirlas a formato FastA en otro archivo output
    dna_sequences.FASTA

CATEGORY
    FASTA format

USAGE
    py src/formatoFASTA.py

ARGUMENTS
    None

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    data/dna_sequences.txt

OUTPUT
    results/dna_sequences.FASTA
'''
# Crear el archivo .txt con secuencias a formatear.
archivoInput = open("data/dna_sequences.txt", "a")

linea1 = "seq_1   ATCGTACGATCGATCGATCGCTAGACGTATCG\n"
linea2 = "seq_2   actgatcgacgatcgatcgatcacgact\n"
linea3 = "seq_3   ACTGAC-ACTGT-ACTGTA----CATGTG"

archivoInput.write(linea1)
archivoInput.write(linea2)
archivoInput.write(linea3)
archivoInput.close()

# Abrir archivo y leer cada línea.
contenido = open("data/dna_sequences.txt", "r")
secSinFormato = contenido.readlines()

# Cerrar el archivo.
contenido.close()

# Crear archivo output .FASTA
archivoOutput = open("results/dna_sequences.FASTA", "a")

# Editar cada secuencia a formato FASTA y escribir en archivo output.
for sec in secSinFormato:
    secLista = sec.split("   ")
    secId = secLista[0]
    secuencia = secLista[1]
    archivoOutput.write("> ")
    archivoOutput.write(str(secId))
    archivoOutput.write("\n")
    archivoOutput.write(str(secuencia.upper().replace("-", "")))

# Cerrar archivo FASTA.
archivoOutput.close()
