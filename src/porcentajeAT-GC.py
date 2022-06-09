'''
NAME: 
    PorcentajeAT-GC.py
    
VERSION:
    4
    
AUTOR: 
    Diana Delgado Gutierrez
    
DESCRIPTION: 
    Programa que calcula el porcentaje de AT y GC con nombre y ruta del archivo input de secuencia.
    
USAGE: 
    python porcentajeAT-GC.py [-h] -i path/to/file [-o OUTPUT] [-r ROUND]
    
ARGUMENTS: 
    -h, --help            show this help message and exit
    -i path/to/file, --input path/to/file
                            File with gene sequences
    -o OUTPUT, --output OUTPUT
                            Path for the output file
    -r ROUND, --round ROUND
                            number of digits to rouond
                        
SOFTWARE REQUIREMENTS: 
    python 3.10
    
INPUT: 
    data/archivo.txt
    
OUTPUT: 
    en pantalla: porcentaje de AT, GC
    results/archivo.txt
'''

import argparse

parser = argparse.ArgumentParser(
    description="Script que calcula el porcentaje de AT-GC en una secuencia.")

parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

parser.add_argument("-o", "--output",
                    help="Path for the output file",
                    required=False)

parser.add_argument("-r", "--round",
                    help="number of digits to rouond",
                    type=int,
                    required=False)

args = parser.parse_args()

# Definir cálculo de porcentajes


def get_AT_content(dna, decimales):
    '''
    Obtiene el porcentaje de AT en una secuencia.

    Parámetros: 
        dna(string): Secuencia de adn.
        decimales(int): Número de decimales a redondear.

    Returns:
        Porcentaje de AT(string)
    '''
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = ((a_count + t_count) / length) * 100
    at_content = round(at_content, decimales)
    return str(at_content)


def get_GC_content(dna, decimales):
    '''
    Obtiene el porcentaje de GC en una secuencia.

    Parámetros: 
        dna(string): Secuencia de adn.
        decimales(int): Número de decimales a redondear.

    Returns:
        Porcentaje de GC(string)
    '''
    length = len(dna)
    g_count = dna.count('G')
    c_count = dna.count('C')
    gc_content = ((c_count + g_count) / length) * 100
    gc_content = round(gc_content, decimales)
    return str(gc_content)


# Checar que la ruta sea viable.
try:
    secuencia = open(args.input, "r")
    dna = secuencia.read().upper()

    try:
        # Comprobar que la secuencia es una secuencia.
        if (dna.isdigit() == True):
            raise ValueError('No hay una secuencia de ADN')

        # Obtener los porcentajes
        porcentajeAT = (get_AT_content(dna, decimales=2))
        porcentajeGC = (get_GC_content(dna, decimales=2))

        # Si quiere que guarde los resultados
        if args.output:
            outputFile = open(args.output, "w")
            print(
                f"Porcentaje de AT: {porcentajeAT}%\n Porcentaje de CG: {porcentajeGC}%",
                file=outputFile)

        print(f"Archivo de la secuencia: {args.input}")
        print(
            f"Porcentaje de AT: {porcentajeAT}%\n Porcentaje de CG: {porcentajeGC}%")

    finally:
        # Cerrar archivo
        secuencia.close()

except IOError as exception:
    print('No se pudo encontrar el archivo: ' + exception.strerror)
