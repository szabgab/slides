import fb

def test_fb(capsys):
    fb.fizzbuzz()
    out, err = capsys.readouterr()
    assert err == ''
    with open('expected.txt') as fh:
        expected = fh.read()
    assert out == expected

