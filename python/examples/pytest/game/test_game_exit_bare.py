import game

def test_immediate_exit():
    input_values = ['x']
    output = []

    def mock_input(s):
       output.append(s)
       return input_values.pop(0)
    game.input = mock_input
    game.print = lambda s : output.append(s)

    game.play()

    assert output == [
        '\nWelcome to another Number Guessing game',
        'Please enter your guess [x|s|d|m|n]: ',
        'x',
        'Sad to see you leave early',
    ]
