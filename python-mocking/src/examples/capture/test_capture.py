import app

def test_myoutput(capsys):
    app.greet("hello", "world")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"

    app.greet("next")
    out, err = capsys.readouterr()
    assert out == "next\n"
    assert err == ""
