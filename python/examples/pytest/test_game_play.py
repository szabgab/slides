import game
import random

def test_immediate_exit():
    input_values = ['30', '50', '42', 'x']
    output = []

    def mock_input(s):
       output.append(s)
       return input_values.pop(0)
    game.input = mock_input
    game.print = lambda s : output.append(s)
    random.randrange = lambda a, b : 42

    game.play()

    assert output == [
        '\nWelcome to another Number Guessing game',
        'Please enter your guess [x|s|d|m|n]: ',
        '30',
        'Your guess is too low',
        'Please enter your guess [x|s|d|m|n]: ',
        '50',
        'Your guess is too high',
        'Please enter your guess [x|s|d|m|n]: ',
        '42',
        'Hit!',
        '\nWelcome to another Number Guessing game',
        'Please enter your guess [x|s|d|m|n]: ',
        'x',
        'Sad to see you leave early',
    ] 
