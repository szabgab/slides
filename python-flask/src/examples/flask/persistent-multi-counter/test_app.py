import app
import os

def test_app(tmpdir):
    os.environ['COUNTER_DATA_DIR'] = str(tmpdir) # str expected, not LocalPath

    web1 = app.app.test_client()
    rv = web1.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'No counter yet. Maybe start by clicking <a href="/python">here</a>'

    rv = web1.get('/python')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/">home</a> python: 1'

    rv = web1.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'''<table>
<tr><td><a href="/python">python</a></td><td>1</td></tr>
</table>'''

    rv = web1.get('/python')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/">home</a> python: 2'

    rv = web1.get('/flask')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/">home</a> flask: 1'

    rv = web1.get('/python')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/">home</a> python: 3'

    rv = web1.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'''<table>
<tr><td><a href="/flask">flask</a></td><td>1</td></tr>
<tr><td><a href="/python">python</a></td><td>3</td></tr>
</table>'''



    web2 = app.app.test_client()
    rv = web2.get('/python')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/">home</a> python: 4'

    rv = web2.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'''<table>
<tr><td><a href="/flask">flask</a></td><td>1</td></tr>
<tr><td><a href="/python">python</a></td><td>4</td></tr>
</table>'''



