import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main' == rv.data

    rv = web.get('/add/2/3')
    assert rv.status == '200 OK'
    assert b'5' == rv.data

    rv = web.get('/mul/2/3')
    assert rv.status == '200 OK'
    assert b'6' == rv.data

    rv = web.get('/sum/2/3/4.1/-1')
    assert rv.status == '200 OK'
    print(rv.data)
    assert b'8.1' == rv.data
