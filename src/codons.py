'''
NAME
    Fasta to codons

VERSION
    2.1

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
    data/seq.nt.fa  formato: fasta

OUTPUT
    results/codons.fasta    formato: fasta
'''
#! /usr/bin/env python34
# Importar librería
from Bio import SeqIO, SeqUtils
from Bio.Seq import Seq

# parsear el archivo fasta en un diccionario
dict = SeqIO.to_dict(SeqIO.parse("data/seq.nt.fa", "fasta"))
id_dict = dict.keys()

# Abrir archivo fasta
fasta = open("results/codons.fasta", "a")

# Encontrar el primer marco de lectura
for id in id_dict:
    # Codón de inicio
    start_codon = SeqUtils.nt_search(str(dict[id].seq), "ATG")
    # Checar que haya marco de lectura
    if len(start_codon) == 1:
        # Si no hay marco de lectura que siga con el siguiente record
        continue
    # Posiciones del codón de inicio
    for j in start_codon[1:]:
        # Para cada uno de los seis marcos de lectura
        for orf in range(3):
            # Separar codones en leading y en lagging
            complement = [str(dict[id].seq.complement()[i:i + 3])
                          for i in range(j + orf, len(str(dict[id].seq)), 3)]
            codones = [str(dict[id].seq[i:i + 3])
                       for i in range(j + orf, len(str(dict[id].seq)), 3)]
            # Quitar los codones que no son tripletes
            if (len(dict[id].seq[j:]) % 3) != 0:
                codones.pop()
                complement.pop()
            # imprimirlos codones separados en formato fasta
            fasta.write(f">{id} en posicion {j+1} marco {orf+1} \n")
            fasta.write(" ".join(codones))
            fasta.write(
                f"\n>{id} complemento en posicion {j+1} en marco {orf+1}\n")
            fasta.write(" ".join(complement))
            fasta.write("\n\n")
