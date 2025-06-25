import app

def test_swap():
    assert app.swap("abcd") == "cdab"
    assert app.swap("abc") == "bca"
    assert app.swap("abcde") == "cdeab"
    assert app.swap("a") == "a"
    assert app.swap("") == ""

def test_average():
    assert app.average(2, 4) == 3
    assert app.average(2, 3) == 2.5
    assert app.average(42) == 42
    #assert app.average() == 0

