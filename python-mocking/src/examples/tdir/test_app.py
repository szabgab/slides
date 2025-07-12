import app
import os

def test_json(tmpdir):
    tdir = str(tmpdir)
    print(tdir)

    data = {
        'name'  : 'Foo Bar',
        'email' : 'foo@bar.com',
    }

    filename = os.path.join(tdir, 'temp.json')
    app.save(filename, data)
    again = app.read(filename)
    assert data == again


