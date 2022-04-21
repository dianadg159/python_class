'''
NAME
    Juego piedra, papel o tijera

VERSION
    1.0

AUTOR
    Diana Delgado Gutierrez

DESCRIPTION
    Un juego donde el usuario puede elegir entre piedra, papel
    o tijera y jugar con la computadora.

USAGE
    py src/piedraPapelTijera.py

ARGUMENTS
    String

SOFTWARE REQUIREMENTS
    Python 3.10

INPUT
    data/4_input_adapters.txt

OUTPUT
    none

'''
# 0. calcular opciones validas.
import random
accionesPosibles = ["piedra", "papel", "tijera"]
# input() al usuario para su opción.
print("Elige una opción (piedra, papel, tijera): ")
eleccionUsuario = input()
eleccionUsuario = eleccionUsuario.lower()
# Función aleatoria de la computadora.
eleccionCompu = random.choice(accionesPosibles)
print(f"La computadora elige: {eleccionCompu}")
# comparar los resultados
# Los dos elegieron lo mismo:
if (eleccionCompu == eleccionUsuario):
    print("¡Empate!")
# tijera gana a papel:
elif ((eleccionCompu == "tijera") & (eleccionUsuario == "papel")):
    print("Perdiste :( ¡Inténtalo de nuevo!")
# papel pierde ante tijera:
elif ((eleccionCompu == "tijera") & (eleccionUsuario == "papel")):
    print("¡Ganaste!")
# piedra gana ante tijera:
elif ((eleccionCompu == "piedra") & (eleccionUsuario == "tijera")):
    print("Perdiste :( ¡Inténtalo de nuevo!")
# tijera pierde ante piedra:
elif ((eleccionUsuario == "piedra") & (eleccionCompu == "tijera")):
    print("¡Ganaste!")
# papel gana ante roca:
elif ((eleccionCompu == "papel") & (eleccionUsuario == "piedra")):
    print("Perdiste :( ¡Inténtalo de nuevo!")
# roca pierde ante papel:
elif ((eleccionUsuario == "papel") & (eleccionCompu == "piedra")):
    print("gana usuario")
# Si el usuario escribió mal:
else:
    print("Escribiste mal tu elección, intenta de nuevo.")
