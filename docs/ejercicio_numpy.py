'''
NAME
    Numpy

VERSION
    1.0

AUTOR
	Diana :)

DESCRIPTION
    Ejercicios de arrays

CATEGORY
    Numpy

USAGE
    py ./data/ejercicio_numpy.py

ARGUMENTS
    none

SOFTWARE REQUIREMENTS
    Python 3.10

OUTPU
    En pantalla
'''
import numpy as np

ecoli_m_b = np.genfromtxt('./data/Biorreactor.csv', delimiter=',')
ecoli_m_b *= 0.39

# Ejercicio 1
# Pasando de g/ml a g/L
prod_g_mL = np.genfromtxt('./data/prod_gml.csv', delimiter=',')
print(prod_g_mL)
prod_g_L = prod_g_mL * 1000
print(prod_g_L)

# Cada gan tiene un inductor diferente.
# Estos inductores tienen diferentes costos.
# Obtener los costos de inductor en cada temperatura.
idx_cost = np.genfromtxt('./data/ind_cost.csv', delimiter=',')
ind_cost_30 = idx_cost * 1.75
ind_cost_35 = idx_cost * 0.8
print(' ')
print(idx_cost)
print(ind_cost_30)
print(ind_cost_35)

# Operaciones sobre arrays
produccion = np.array([[16, 14], [12, 9], [8, 15]])
print()
print(produccion)
# suma
produccion *= 2
suma_col = np.sum(produccion, axis=0)
print(produccion)
print(suma_col)
suma_fila = np.sum(produccion, axis=1)
print(suma_fila)
# Del total del metabolito necesito 5 unidades
# ¿cuanto me queda?
metab_resta = suma_col - 5
print(metab_resta)
# Para la misma cantidad de metabolito
# ¿Cuanto me falta/sobra de metabolito A?
print(metab_resta[0] - metab_resta[1])
# ¿y si fuera por bacteria?
extra_x_bact = produccion[:, 0] - produccion[:, 1]
print(extra_x_bact)
#   ejemplos
print(produccion[1::2, 0])
print(produccion[2::-1, 0])

# Ejercicio 2
# Obtener los costos de produccion por cada g/L a 30°
# costo
# 3.5*1.75 = 5
# x = 1
# x = (1*(3.5*1.75))/5
print(prod_g_L[:, 0])
cost_x_g = ind_cost_30 * 1 / prod_g_L[:, 0]
print(cost_x_g)

# Booleanos
boo_mayor_0 = extra_x_bact > 0
print(extra_x_bact[boo_mayor_0])

# Ejercicio3
# ¿en algun caso es mas barato producir en 30° en lugar de 35°?
genes = np.array(["Gen1", "Gen2", "Gen3", "Gen4"])
cost_x_g_30 = ind_cost_30 * 1 / prod_g_L[:, 0]
cost_x_g_35 = ind_cost_35 * 1 / prod_g_L[:, 0]
print(cost_x_g_30)
print(cost_x_g_35)
barato_30 = cost_x_g_30 - cost_x_g_35
bool_barato = barato_30 < 0
print(genes[bool_barato])
