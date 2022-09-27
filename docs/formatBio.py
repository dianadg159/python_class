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


def qualityRecords(archivo, umbral):
    qlectures = 0
    for record in SeqIO.parse(archivo, "fastq"):
        qscores = record.letter_annotations["phred_quality"]
        qscores.sort()
        if qscores[0] >= umbral:
            qlectures += 1
            with open("qualityIds", "a") as ids:
                ids.write(record.id + "\n")
                ids.write(record.seq + "\n")
                ids.close()
    return("Número de ids con bases de calidad" + str(qlectures))


qualityRecords("data/sample.fastq", 36)
'''
for i in qscores:
    if str(i) >= qvalue:
        qlecture += 1
print(qlecture)
'''
