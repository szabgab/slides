import api

def test_echo():
    web = api.app.test_client()

    rv = web.get('/echo?text=hello')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json ==  {'res': 'Text: hello'}

    rv = web.post('/echo', data={'text': 'ciao'})
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {'Answer': 'You said: ciao'}


    # If the parameter is missing the parser just returns None
    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json ==  {'res': 'Text: None'}
