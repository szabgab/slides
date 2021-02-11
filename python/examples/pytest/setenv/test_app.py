import app
import os

def test_python():
    out = app.get_python_version()
    assert out == 'Python 3.8.6\n'

def test_in_path(monkeypatch):
    monkeypatch.setenv('PATH', '/usr/bin')
    out = app.get_python_version()
    assert out == 'Python 2.7.18\n'
    print(os.environ['PATH'])


def test_other():
    print(os.environ['PATH'])
