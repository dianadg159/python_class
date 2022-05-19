# Funciones
```
def functionName(args):
    <código>
    return var
```
Si un programa no requiere return pq imprimen un resultado o modifican otra parte del código.
Podemos asignar valores default en el paso de argumentos en una función. 
Es mejor pasar el argumento cuando se llama la fxn, como buena práctica no usar valores por default. 

### assert
Definir los casos específicos en donde el código debe funcionar.
Pruebas para saber que el código soporta los argumentos que le dan a la función.
solo se usa con casos de uno o pruebas y posteriormente se puede eliminar.
` assert <prueba> == <resultado esperado> `