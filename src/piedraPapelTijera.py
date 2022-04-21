
# Pedir al usuario su opción

# La computadora obtiene su opción

# tijera gana al papel

# tijera pierde contra roca

# papel gana a roca

# papel pierde ante tijera

# piedra gana ante tijera

# piedra pierde ante papel

# iguales es empate

'''
0. calcular opciones validas.
possible_actions = ["rock", "paper", "scissors"]
1. input() al usuario para su opción.
user_action = input("Enter a choice (rock, paper, scissors): ")
2. Función aleatoria de la computadora.
computer_action = random.choice(possible_actions)
3. comparar los resultados
    - if (computer_action == user_action)
        print("empate")
    tijera gana a papel:
    -elif ((computer_action == tijera) & (user_action == papel))
        print("gana computadora")
    papel pierde ante tijera:
    -elif ((user_action == tijera) & (computer_action == papel))
        print("gana usuario")
    roca gana ante tijera:
    -elif ((computer_action === roca) & (user_action == tijera))
        print("gana computadora")
    tijera pierde ante roca:
    -elif ((user_action == roca) & (computer_action = tijera))
        print("gana usuario")
    papel gana ante roca:
    -elif ((computer_action == papel) & (user_action == roca))
        print("gana computadora")
    roca pierde ante papel:
    -elif ((user_action == papel) & (computer_action == roca))
        print("gana usuario")
'''
