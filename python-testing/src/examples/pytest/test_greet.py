from greet import welcome

def test_myoutput(capsys):
    welcome("hello", "world")
    out, err = capsys.readouterr()
    assert out == "STDOUT: hello\n"
    assert err == "STDERR: world\n"

    welcome("next")
    out, err = capsys.readouterr()
    assert out == "STDOUT: next\n"
    assert err == ""
