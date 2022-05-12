## Interfaz de línea de comandos
Existen programas con argumentos posicionales u opcionale.
Algunos comandos tienen una mezcla de ambos. 
Los posicionales son donde el orden donde paso los argumentos importa, los opcionales es cuando los argumentos o tienen un orden definido.
Ejemplo general: `[Nombre del porgrama] [opción] [valor]`

### Argumento de línea de comandos en Python
inicializar parser con .ArgumentParser()
luego se leen los argumentos con .parse_args
todo en Python es un objeto

Namespace()
colección de identificadores. 
variables globales: en todo el programa.
dentro de in for hay una variable y es una variable local.
Python le pone el nombre que viene después del --
