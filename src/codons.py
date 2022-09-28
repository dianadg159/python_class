'''
NAME
    Fasta to codons

VERSION
    2.0

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
# from Bio import SeqUtils
from Bio.Seq import Seq

# parsear el archivo fasta en un diccionario
dict = SeqIO.to_dict(SeqIO.parse("data/seq.nt.fa", "fasta"))
id_dict = dict.keys()

# Encontrar el primer marco de lectura
for id in id_dict:
    # Codón de inicio
    # start_codon = SeqUtils.nt_search(str(dict[id].seq), "TAC")
    # Checar que haya marco de lectura
    # if len(start_codon) == 1:
    # Si no hay marco de lectura que siga con el siguiente record
    # continue
    # else:
    # Posición del primer codón
    for j in range(3):
        # Separar codones en leading y en lagging
        complement = [str(dict[id].seq.complement()[i:i + 3])
                      for i in range(j, len(str(dict[id].seq)), 3)]
        codones = [str(dict[id].seq[i:i + 3])
                   for i in range(j, len(str(dict[id].seq)), 3)]
        # Quitar los codones que no son tripletes
        if (len(dict[id].seq[j:]) % 3) != 0:
            codones.pop()
            complement.pop()
        # imprimirlos codones separados en formato fasta
        print(f">{id} en marco {j+1}")
        print(*codones)
        print(f">{id} complemento en marco {j+1}")
        print(*complement)
        print("\n")
