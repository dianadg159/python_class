'''
NAME
    Fasta to codons
    
VERSION
    1.1

AUTOR
	Diana :)

DESCRIPTION
    Imprime los codones separados por un espacio desde un
    archivo tipo fasta

CATEGORY
    FASTA

USAGE
    py ./src/codons.py

ARGUMENTS
    none

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    formato de archivo: fasta

OUTPUT
    Imprime en pantalla los codones con encabezado tipo fasta.
'''
#! /usr/bin/env python34
# Importar librería
from Bio import SeqIO
from Bio import SeqUtils

# parsear el archivo fasta en un diccionario
dict = SeqIO.to_dict(SeqIO.parse("data/seq.nt.fa", "fasta"))
id_dict = dict.keys()

# Encontrar el primer marco de lectura
for id in id_dict:
    # Codón de inicio
    start_codon = SeqUtils.nt_search(str(dict[id].seq), "TAC")
    # Checar que haya marco de lectura
    if len(start_codon) == 1:
        # Si no hay marco de lectura que siga con el siguiente record
        continue
    else:
        # Posición del primer codón
        start = start_codon[1]
        # Separar codones
        codones = [str(dict[id].seq[i:i + 3])
                   for i in range(start, len(str(dict[id].seq)), 3)]
        if (len(dict[id].seq[start:]) % 3) != 0:
            codones.pop()
        # imprimirlos codones separados
        print(f">{id}")
        print(*codones)
