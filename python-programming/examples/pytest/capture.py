import sys

def greet(to_out, to_err=None):
    print(to_out)
    if to_err:
        print(to_err, file=sys.stderr)


def test_myoutput(capsys):
    greet("hello", "world")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"

    greet("next")
    out, err = capsys.readouterr()
    assert out == "next\n"
