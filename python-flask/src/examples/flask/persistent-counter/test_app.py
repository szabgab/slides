import app
import os

def test_app(tmpdir):
    os.environ['COUNTER_DATA_DIR'] = str(tmpdir) # str expected, not LocalPath

    web1 = app.app.test_client()
    rv = web1.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'1'

    rv = web1.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'2'

    web2 = app.app.test_client()
    rv = web2.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'3'


