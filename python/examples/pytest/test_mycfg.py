import mycfg
import os

def test_parse():
    data = mycfg.parse_file('a.cfg')
    assert data, {
        'name'  : 'Foo Bar',
        'email' : 'foo@bar.com',
    }

def test_example(tmpdir):
    original = {
        'name'  : 'My Name',
        'email' : 'me@home.com',
        'home'  : '127.0.0.1',
    }
    filename = str(tmpdir.join('abc.cfg'))
    assert not os.path.exists(filename)
    mycfg.save_file(filename, original)
    assert os.path.exists(filename)
    new = mycfg.parse_file(filename)
    assert new == original
