'''
NAME
    Formatear secuencia a Fasta
    
VERSION
    1.0

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
# Crear el archivo .txt con las secuencias sin formato.
archivoInput = open("data/dna_sequences.txt", "a")

linea1 = "seq_1   ATCGTACGATCGATCGATCGCTAGACGTATCG\n"
linea2 = "seq_2   actgatcgacgatcgatcgatcacgact\n"
linea3 = "seq_3   ACTGAC-ACTGT-ACTGTA----CATGTG"

archivoInput.write(linea1)
archivoInput.write(linea2)
archivoInput.write(linea3)
archivoInput.close()

# Abrir el archivo para leer línea por línea y guardar el contenido
# en una lista.
contenido = open("data/dna_sequences.txt", "r")
secSinFormato = contenido.readlines()

# Cerrar el archivo.
contenido.close()

# Crear un archivo output .FASTA
archivoOutput = open("results/dna_sequences.FASTA", "a")

# Cortar la primera parte de la secuencia para usarla de encabezado.
for sec in secSinFormato:
    secLista = sec.split("   ")
    secId = secLista[0]
    secuencia = secLista[1]
    # Editar cada una de las secuencias a un formato FASTA y escribirlas
    # en el archivo .FASTA
    archivoOutput.write("> ")
    archivoOutput.write(str(secId))
    archivoOutput.write("\n")
    archivoOutput.write(str(secuencia.upper().replace("-", "")))

# Cerrar archivo FASTA
archivoOutput.close()
