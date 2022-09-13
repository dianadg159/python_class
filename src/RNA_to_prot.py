'''
NAME: 
    RNA to Protein
    
VERSION:
    1.2
    
AUTOR: 
    Diana Delgado Gutierrez
    
DESCRIPTION: 
    Programa que traduce una secuencia de ARN a una cadena 
    de aminoácidos. 
    
USAGE: 
    python RNA_to_prot.py [-h] -s secuenciaRNA
    
ARGUMENTS: 
    -h, --help            show this help message and exit
    -s, --string          string de RNA a traducir
                        
SOFTWARE REQUIREMENTS: 
    python 3.10
    
INPUT: 
    secuencia de RNA
    
OUTPUT: 
    en pantalla: cadema de aminoácidos
'''
# Importando librería
import argparse
import re

# Input
parser = argparse.ArgumentParser(
    description="Script que traduce secuencias de ARN.")
parser.add_argument("-s", "--string",
                    help="String con secuencia de ARN.",
                    required=True)

# Asignar variables al input.
argumentos = parser.parse_args()
rna = argumentos.string.upper()

# Verificar si no es secuencia de RNA
if re.search(f"[^GCATU]", rna):
    print("Por favor introduce vuelve a checar que tu secuencia sea RNA o DNA")
    quit()
rna = rna.replace('U', 'T')

# Hacer un diccionario
gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

# Hacer una lista de codones.
codones = [rna[i:i + 3] for i in range(0, len(rna), 3)]

# LLamar al diccionario
peptido = [gencode.get(codon) for codon in codones]
peptido.remove("_")

# Imprimir a pantalla el péptido
print("La secuencia de aa es: " + "".join(peptido))
