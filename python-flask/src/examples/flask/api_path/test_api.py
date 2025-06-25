import api

def test_echo():
    web = api.app.test_client()

    rv = web.get('/echo/hello')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json ==  {'res': 'Text: hello'}


    rv = web.post('/echo/ciao')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {'Answer': 'You said: ciao'}
