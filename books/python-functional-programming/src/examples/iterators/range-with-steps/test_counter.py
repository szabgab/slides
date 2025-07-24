import it

def test_range():
    r = it.Range(1, 6, 2.2)
    result = list(r)
    assert result == [1, 3.2, 5.4]
