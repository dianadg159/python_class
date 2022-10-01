#! /usr/bin/env python3
# Importar librería
from Bio.Seq import MutableSeq
from Bio.SeqUtils import nt_search

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
print(dnaseq.translate(to_stop=True, cds=False))

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
'''

# ciclo para checar todas las cadenas respecto a las posiciones encontradas

# obtener codones de inicio
adn = MutableSeq(
    "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
posicion = nt_search(str(adn), "ATG")


def nombre(secuencia, posicion):
    # lista longitud de las proteinas encontradas
    long_proteina = []
    prots = []
    for i in range(1, len(posicion)):
        # ajuste debido a inicio de codon
        ajuste = posicion[i]
        # usando el ajuste tomaremos solo la parte correcta
        sec_prot = secuencia[ajuste:]
        # traducir sec_prot y contemplar el codon de paro
        proteina = sec_prot.translate(to_stop=True)
        prots.append(str(proteina))
        # checar longitud
        long_proteina.append(len(proteina))
    # checar cual fue la longitud mas grande
    return(prots, max(long_proteina))


tupla = nombre(adn, posicion)
pept = tupla[0]
max_length = tupla[1]
for j in range(len(pept)):
    if len(pept[j]) == max_length:
        print("Cadena con mayor longitud:")
        print(pept[j])
