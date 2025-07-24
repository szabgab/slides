import api

def test_echo():
    web = api.app.test_client()

    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"prompt": "Type in something"}


    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "This"}
