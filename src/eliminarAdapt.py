'''
NAME
    Eliminar adaptador de secuencias

VERSION
    2

AUTOR
    Diana Delgado Gutierrez

DESCRIPTION
    A partir de un archivo .txt crear otro archivo con la misma secuencia
    sin unas regiones de la secuencia (adaptadores).

USAGE
    py src/eliminarAdapt.py

ARGUMENTS
    String

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    data/4_input_adapters.txt

OUTPUT
    results/4_output_noAdapters.txt

'''
try:
    # Leer el archivo línea por línea.
    contenido = open("data/4_input_adapter.txt", "r")
    secuencias = contenido.readlines()
    contenido.close()

    # Crear un archivo output.
    secNoAdapt = open("results/4_output_adapters.txt", "w")

    # Recorrer la lista y eliminar adaptador.
    for sec in secuencias:
        secNoAdapt.write(str(sec[14:-1]))
        secNoAdapt.write("\n")
    secNoAdapt.close()
except IOError as ex:
    print("No se encuentra el archivo: " + ex.filename)
