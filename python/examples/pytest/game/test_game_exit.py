import game
import sys
import io

def test_immediate_exit(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('x'))

    game.play()
    out, err = capsys.readouterr()
    assert err == ''

    expected = '''
Welcome to another Number Guessing game
Please enter your guess [x|s|d|m|n]: x
Sad to see you leave early
'''
    assert out == expected
