import app
import io
import sys

def test_app(capsys):
    sys.stdin = io.StringIO('Foo')
    app.ask_one()
    out, err = capsys.readouterr()
    assert err == ''
    #print(out)
    assert out == 'Please enter your name: Your name is Foo\n'
