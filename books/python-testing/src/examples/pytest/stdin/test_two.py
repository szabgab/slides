import app
import io
import sys

def test_app(capsys):
    sys.stdin = io.StringIO('3\n4')
    app.ask_two()
    out, err = capsys.readouterr()
    assert err == ''
    #print(out)
    assert out == 'Please enter width: Please enter length: 3.0*4.0 is 12.0\n'
