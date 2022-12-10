#! /usr/bin/env python3
import pandas as pd
# series
ecoli_matraz = pd.Series([0.1, 0.15, 0.19, 0.5],
                         name='Matraz'
                         )
ecoli_matraz


costos = pd.Series([5, 4.5, 7, 3.5], index=['gen5', 'gen2', 'gen3', 'gen1'])
produccion = pd.Series([5, 11, 4, 7, 2], index=[
                       'gen1', 'gen2', 'gen3', 'gen4', 'gen5'])
# Multiplicacion
# Busca los índices que son iguales, no importa la posicion
#print(costos * produccion)
# Ordenar según index
# print(produccion.sort_index(ascending=False))
# Ordenar por valores
# print(produccion.sort_values(ascending=True))
# cuantos elementos hay en la serie
# print(produccion.count())

#
prot_genes = pd.read_csv('./data/prot_genes.csv',
                         index_col='Organism', squeeze=True)
num_genes = pd.read_csv('./data/num_genes.csv',
                        index_col='Organism', squeeze=True)
top_5_genoma_big = num_genes.sort_values(ascending=False).head()
# print(top_5_genoma_big)
# genes -> Num total del genoma
# prot_g -> Num de genes que codifican para proteína
# sort
top_5_genoma_big = num_genes.sort_values(ascending=False).head()
top5_idx = top_5_genoma_big.index
# head
prot_genes[top5_idx]
# bool
# print(top_5_genoma_big.plot.bar())
# Contar organismos
organism = pd.read_csv('./data/Organism.csv', squeeze=True)
product = pd.read_csv('./data/Org_prod.csv', squeeze=True)
print(organism.value_counts())
ax = organism.value_counts().plot.bar()
fig = ax.get_figure()
fig.savefig('./docs/figure.pdf')

# Hacerlos listas
#print(organism.str.split(' '))
# Hacer booleanos
nuevo_nombre = organism[organism == 'Saccharomyces cerevisiae'] + '(Hongo)'
print(nuevo_nombre)

organism = pd.read_csv('./data/Organism.csv',
                       squeeze=True)
bacteria = ['Escherichia coli', 'Cupriavidus necator']
hongo = ['Saccharopolyspora erythraea', 'Saccharomyces cerevisiae']
organism[organism.isin(bacteria)] = 'Grupo_1'
organism[organism.isin(hongo)] = 'Grupo_2'
print(organism.head())
