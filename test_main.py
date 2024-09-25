import pytest
from unittest.mock import patch
from src.jugador import player_turn
from src.computadora import computer_turn

def test_game_stops_after_player_wins():
    random_number = 50

    with patch('builtins.input', return_value="50") as mock_input, \
         patch('src.computadora.computer_turn', return_value=False) as mock_computer:
        result = player_turn(random_number)
    
        assert result is True 
        mock_computer.assert_not_called()  

def test_game_stops_after_computer_wins():
    random_number = 50

    with patch('builtins.input', return_value="30") as mock_input, \
         patch('random.randint', return_value=50) as mock_rand:
        result = computer_turn(random_number)
    
        assert result is True  
        mock_input.assert_not_called()  