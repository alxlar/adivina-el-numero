from unittest.mock import patch
from src.computadora import computer_turn

def test_computer_wins():
    random_number = 50

    with patch('random.randint', return_value=50):
        result = computer_turn(random_number)
    
    assert result is True 

def test_computer_does_not_win():
    random_number = 50

    with patch('random.randint', return_value=30):
        result = computer_turn(random_number)
    
    assert result is False 
