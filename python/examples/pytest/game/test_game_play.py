import game
import random
import sys
import io

def test_immediate_exit(monkeypatch, capsys):
    input_values = '\n'.join(['30', '50', '42', 'x'])
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))

    monkeypatch.setattr(random, 'randrange', lambda a, b : 42)

    game.play()
    out, err = capsys.readouterr()

    assert out == '''
Welcome to another Number Guessing game
Please enter your guess [x|s|d|m|n]: 30
Your guess is too low
Please enter your guess [x|s|d|m|n]: 50
Your guess is too high
Please enter your guess [x|s|d|m|n]: 42
Hit!

Welcome to another Number Guessing game
Please enter your guess [x|s|d|m|n]: x
Sad to see you leave early
'''
