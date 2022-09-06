# Clases y Objetos
class animal():
    # Atributos de instancia
    nombre = ''
    edad = 0
    peligro = 0
    especie = ''
    altura = 0
    peso = 0
    progenie = 0
    alimentacion = ''

    # Método para que haga ruido
    def haz_ruido(self):
        print('guau')

    # Método para hacer un objeto.
    def __init__(self, nombre, alimentacion, altura, peso, progenie):
        self.nombre = nombre
        self.alimentacion = alimentacion
        self.altura = altura
        self.peso = peso
        self.progenie = progenie


class perro(animal):
    ternura = 100


class gato(animal):
    ternura = 10
    usa_arenero = True


Shagui = perro('Shagui', 'croquetas', 25, 15, 0)
Quien_sabe = gato('Quien sabe', 'Wiskas', 14, 5, 0)

print(f"El gato usa arenero? {gato.usa_arenero}")
print("Ternura del gato : " + str(gato.ternura))

print("Ternura del perro: " + str(perro.ternura))
print("Nivel de peligro del perro: " + str(perro.peligro))
