
# Pedir al usuario su opción

# La computadora obtiene su opción

# tijera gana al papel

# tijera pierde contra roca

# papel gana al papel

# papel pierde ante

# iguales es empate

'''
0. calcular opciones validas.
possible_actions = ["rock", "paper", "scissors"]
1. input() al usuario para su opción.
user_action = input("Enter a choice (rock, paper, scissors): ")
2. Función aleatoria de la computadora.
computer_action = random.choice(possible_actions)
3. comparar los resultados
    - if (computadora == usuario)
        print("empate")
    -elif ((computadora = tijera) & (usuario = papel))
        print("gana computadora")
    -elif ((usuario = tijera) & (computadora = papel))
        print("gana usuario")
    -elif ((computadora = roca) & (usuario = tijera))
        print("gana computadora")
    -elif ((usuario = roca) & (computadora = tijera))
        print("gana usuario")
    -elif ((computadora = papel) & (usuario = roca))
        print("gana computadora")
    -elif ((usuario = papel) & (computadora = roca))
        print("gana usuario")
        
        
    Si usuario = roca entonces
        si computadora = papel
            Imprimir "computadora gana"
        de otra manera /computadora = tijeras
            imprimir "usuario gana" 
    si usuario = papel entonces
        si computadora = tijeras
            Imprimir "computadora gana"
        de otro modo /computadora = roca
            imprimir "usuario gana"
    si usuario = tijeras entonces
        si computadora = roca
            imprimir "computadora gana"
        de otro modo / computadora = papel
            imprimir "usuario gana"
convertir todo a minúsculas del input del usuario.
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

'''
