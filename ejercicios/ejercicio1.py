'''
Encabezado  
'''
saludo = "Buenos dias"
nombre = "Andrea"
mensaje = saludo + ' ' + nombre
mensaje += '!'

print(len(mensaje))
# para usar el método se usa '.metodo' después del objeto al que va asociado.
print(mensaje.find('Andrea'))
print(mensaje.find('Kevin'))

# ¿Dode empieza el codón inicial AUG (TAC) en la secuencia?
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
print(f"El codón de inicio está en la posición: {dna.find('TAC')}")

print(mensaje.lower())
print(mensaje.upper())

# Buscar tipos de varibles y sus métodos asociados. Los más usados.
