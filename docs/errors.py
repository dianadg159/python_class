import os
t = open()
try:
    f = open('data/7-file_num.txt')
    my_number = int(f.read())
except IOError as exception:
    print("sorry, couldn't open the file: " + exception.strerror)
except ValueError as exception:
    print("sorry, couldn't parse the number " + exception.args[0])
# args nos da los argumentos del programa donde la primera posiccion es el nombre del programa.
# nos va a regresar el mensaje en la primera celda del error en ValueError
else:
    print(my_number + 5)
