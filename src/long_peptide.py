'''
NAME
    Péptido más largo

VERSION
    1.1

AUTOR
	Diana :)

DESCRIPTION
    Con una secuancia determinada determinar la cadena
    protéica de mayor longitud

CATEGORY
    Proteins

USAGE
    py ./src/long_peptide.py

ARGUMENTS


SOFTWARE REQUIREMENTS
    Python 3.10

INPUT

 [files or directories used to run the program and formats]

OUTPUT

[file names and formats]
'''

#! /usr/bin/env python3
# Importar librería
from Bio.Seq import MutableSeq, Seq
from Bio.SeqUtils import nt_search
# ciclo para checar todas las cadenas respecto a las posiciones encontradas

# obtener codones de inicio
adn = MutableSeq(
    "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
posicion = nt_search(str(adn), "ATG")


def traduccion(secuencia, posicion):
    # lista longitud de las proteinas encontradas
    long_proteina = []
    prots = []
    for i in range(1, len(posicion)):
        # ajuste debido a inicio de codon
        ajuste = posicion[i]
        # usando el ajuste tomaremos solo la parte correcta
        sec_prot = secuencia[ajuste:]
        # Ver que la secuencia sea multiplo de tres
        residuo = len(sec_prot) % 3
        # Quitar el warning
        if residuo != 0:
            # Asegurarse de que la secuencia sea multiplo de tres
            sec_prot = sec_prot + Seq("N" * (3 - residuo))
        # traducir sec_prot y contemplar el codon de paro
        proteina = sec_prot.translate(to_stop=True)
        prots.append(str(proteina))
        # checar longitud
        long_proteina.append(len(proteina))
    # checar cual fue la longitud mas grande
    return(prots, max(long_proteina))


def longitud(tupla):
    pept = tupla[0]
    max_length = tupla[1]
    for j in range(len(pept)):
        if len(pept[j]) == max_length:
            print("Cadena con mayor longitud:")
            print(pept[j])


tupla = traduccion(adn, posicion)
longitud(tupla)
