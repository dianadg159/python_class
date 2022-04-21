'''
NAME
    Juego piedra, papel o tijera

VERSION
    1.0.1

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
    archivos: none
    en pantalla: Elección del usuario (piedra, papel o tijera).

OUTPUT
    archivos: none
    en pantalla: Elección de la computadora y quién ganó.

'''
# Definir las opciones validas a elegir.
import random
accionesPosibles = ["piedra", "papel", "tijera"]

# Pedir al usuario para su elección.
print("Elige una opción (piedra, papel, tijera): ")
eleccionUsuario = input()
eleccionUsuario = eleccionUsuario.lower()

# Elección aleatoria de la computadora.
eleccionCompu = random.choice(accionesPosibles)
print(f"La computadora elige: {eleccionCompu}")

# Comparar los resultados.
# Los dos elegieron lo mismo:
if (eleccionCompu == eleccionUsuario):
    print("¡Empate!")

# Papel pierde ante tijera:
elif ((eleccionCompu == "tijera") & (eleccionUsuario == "papel")):
    print("Perdiste :( ¡Inténtalo de nuevo!")
# papel gana ante piedra:
elif ((eleccionCompu == "piedra") & (eleccionUsuario == "papel")):
    print("¡Ganaste!")

# tijera pierde ante piedra:
elif ((eleccionCompu == "piedra") & (eleccionUsuario == "tijera")):
    print("Perdiste :( ¡Inténtalo de nuevo!")
# tijera gana ante papel:
elif ((eleccionCompu == "papel") & (eleccionUsuario == "tijera")):
    print("¡Ganaste!")

# piedra pierde ante papel:
elif ((eleccionCompu == "papel") & (eleccionUsuario == "piedra")):
    print("Perdiste : ¡Inténtalo de nuevo!")
# piedra gana ante tijera:
elif ((eleccionCompu == "tijera") & (eleccionUsuario == "piedra")):
    print("¡Ganaste!")

# Si el usuario escribió mal:
else:
    print("Escribiste mal tu elección, intenta de nuevo.")
