from unittest.mock import patch
from src.jugador import player_turn

def test_player_wins():
    random_number = 50

    with patch('builtins.input', return_value="50"):
        result = player_turn(random_number)
    
    assert result is True  

def test_player_does_not_win():
    random_number = 50

    with patch('builtins.input', return_value="30"):
        result = player_turn(random_number)
    
    assert result is False  
