import game

def test_immediate_exit(monkeypatch, capsys):
    input_values = ['x']

    def mock_input(s):
       print(s)
       return input_values.pop(0)
    game.input = mock_input

    game.play()
    out, err = capsys.readouterr()
    assert err == ''

    expected = '''
Welcome to another Number Guessing game
Please enter your guess [x|s|d|m|n]: 
x
Sad to see you leave early
'''
    assert out == expected
