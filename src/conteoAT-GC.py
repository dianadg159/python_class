'''
NAME:
    Conteo de A,C,G y T
    
VERSION:
    2.1
    
AUTOR:
    Diana Delgado Gutierrez
    
DESCRIPTION:
    Programa que cuente el total de A,C,G y T que hay en una secuencia de DNA introducida por el usuario.
    
USAGE:
    py conteoAT-GC.py [-h] -s SEC
    
ARGUMENTS:
    -h, --help         show this help message and exit
    -s SEC, --sec SEC  Secuencia de adn.
    
SOFTWARE REQUIREMENTS:
    python 3.10
    
INPUT:
    en pantalla: string de secuencia de adn.
    
OUTPUT:
    en pantalla: porcentaje de AT y GC
    
'''
import argparse

# Pedir la secuencia de DNA al usuario.
parser = argparse.ArgumentParser(
    description="Script que cuenta contenido de AT y GC en una secuencia.")

parser.add_argument("-s", "--sec",
                    help="Secuencia de adn.",
                    type=str.upper,
                    required=True)

# Pedir los datos
argumentos = parser.parse_args()
dna = argumentos.sec

# Generar un ValueError cuando no se da una secuencia de ADN.
if (dna.count('A') == 0 & dna.count('T') == 0 & dna.count('C') == 0 & dna.count('G') == 0):
    raise ValueError('Lo que introduciste no es una secuencia de ADN.')

# La cantidad de A, T, C y G.


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
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return str(round(at_content, decimales))


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
    gc_content = (c_count + g_count) / length
    return str(round(gc_content, decimales))


print("Contenido de AT: " + get_AT_content(dna, 2))
print("Contenido de GC: " + get_GC_content(dna, 2))
