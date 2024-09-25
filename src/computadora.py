import random

def computer_turn (random_number):
    print("""
          ✧✧✧✧✧ Ronda de la computadora 🤖 ✧✧✧✧✧
          """)
    
    computer_prediction = random.randint(1, 100)
    print("La computadora cree que es:", computer_prediction)
    
    if computer_prediction == random_number:
        print("PERDISTE :(, GANÓ LA COMPUTADORA")
        return True
    elif computer_prediction > random_number:
        print("Pista: Más bajo 🔻")
    else:
        print("Pista: Más alto 🔺")
    
    return False