import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<button id="calc">Calc</button>' in rv.data

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

    rv = web.get('/api/calc?a=7&b=8')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  7,
        "b"        :  8,
        "add"      :  15,
        "multiply" :  56,
        "subtract" :  -1,
        "divide"   :  0.875,
    }

    rv = web.get('/api/calc', query_string={ 'a' : '10', 'b': '2' })
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  10,
        "b"        :  2,
        "add"      :  12,
        "multiply" :  20,
        "subtract" :  8,
        "divide"   :  5,
    }

