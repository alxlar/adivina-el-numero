import random
from jugador import player_turn
from computadora import computer_turn

random_number = random.randint(1, 100)
current_turn = True

while current_turn:
    if player_turn(random_number):
        break

    if computer_turn(random_number):
        break
