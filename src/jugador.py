def player_turn (random_number):
    print("""
          ✧✧✧✧✧ Ronda del Jugador👤 ✧✧✧✧✧
          """)
    player_prediction = int(input("¿Qué número crees que es? "))
    
    if player_prediction == random_number:
        print("GANASTE! :D")
        return True
    elif player_prediction > random_number:
        print("Pista: Más bajo 🔻")
    else:
        print("Pista: Más alto 🔺")
    
    return False