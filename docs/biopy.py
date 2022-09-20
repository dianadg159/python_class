#! /usr/bin/env python3
# Importar librería
from Bio.Seq import MutableSeq

# Obtener cadena protéica de cualquiera de sus ORFs

# Cadena a traducir
adn = MutableSeq(
    "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

# Input sobre qué ORF usar
'''print('En qué ORF deseas traducir? (1, 2 o 3?)')
orf = int(input())

# Modificar la secuencia para no tener errores.
if orf == 2:
    adn += "N"
elif orf == 3:
    adn += "NN"

# Determinar la secuacia a partir del ORF
dnaseq = adn[orf - 1:]
print(dnaseq.translate(to_stop=True, cds=False))'''

dnaseq1 = adn
dnaseq2 = adn[1:]
dnaseq3 = adn[2:]

peptide1 = dnaseq1.translate(to_stop=True, cds=False)
peptide2 = dnaseq2.translate(to_stop=True, cds=False)
peptide3 = dnaseq3.translate(to_stop=True, cds=False)

if len(peptide1) > len(peptide2):
    if len(peptide2) > len(peptide3):
        print(peptide1 + '1')
    elif len(peptide3) > len(peptide1):
        print(peptide3 + '3')
    else:
        print(peptide1 + '1')
elif len(peptide2) > len(peptide1):
    if len(peptide1) > len(peptide3):
        print(peptide2 + '2')
    elif len(peptide3) > len(peptide2):
        print(peptide3 + '3')
    else:
        print(peptide2 + '2')
