import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main <a href="/api/info">info</a>' in rv.data

    rv = web.get('/api/info')
    assert rv.status == '200 OK'
    #print(rv.data) # the raw json data
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
       "ip" : "127.0.0.1",
       "hostname" : "everest",
       "description" : "Main server",
       "load" : [ 3.21, 7, 14 ]
    }

