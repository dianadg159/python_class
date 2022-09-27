#! /usr/bin/env python3
# Importar librería

from Bio import SeqIO
import numpy as np

# guardar id's de interés
seq_ids = ['KX886266.1']
with open("data/filtered.fasta", "w") as out_handle:
    for record in SeqIO.parse("data/prueba.fasta", "fasta"):
        if record.id in seq_ids:
            SeqIO.write(record, out_handle, "fasta")

# como checariamos el tamaño del genoma
# NC_050871.1
archivo = 'data/prueba.fasta'

for seq in SeqIO.parse(archivo, "fasta"):
    # solo nos interesa el genoma completo
    if seq.id == 'NC_050871.1':
        # imprima tamaño de seq
        print(len(seq.seq))


print("¿Cuál es el mínimo de score?")
qvalue = input()
qlectures = 0
for record in SeqIO.parse("data/sample.fastq", "fastq"):
    qscores = record.letter_annotations["phred_quality"]
    prom = np.mean(qscores)
    if str(prom) >= qvalue:
        qlectures += 1
print(qlectures)
'''
for i in qscores:
    if str(i) >= qvalue:
        qlecture += 1
print(qlecture)
'''
