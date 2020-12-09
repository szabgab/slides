import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Calculator' in rv.data

    rv = web.get('/api/add', query_string={ 'a' : '10', 'b': '2' })
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  10,
        "b"        :  2,
        "add"      :  12,
    }

#    rv = web.get('/api/multiply', query_string={ 'a' : '11', 'b': '2' })
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    resp = rv.json
#    assert resp == {
#        "a"        :  11,
#        "b"        :  2,
#        "multiply" :  22,
#    }
#
#    rv = web.get('/api/subtract', query_string={ 'a' : '7', 'b': '2' })
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    resp = rv.json
#    assert resp == {
#        "a"        :  7,
#        "b"        :  2,
#        "subtract" :  5,
#    }
#
#
#    rv = web.get('/api/calc', query_string={ 'a' : '10', 'b': '2' })
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    resp = rv.json
#    assert resp == {
#        "a"        :  10,
#        "b"        :  2,
#        "add"      :  12,
#        "multiply" :  20,
#        "subtract" :  8,
#        "divide"   :  5,
#    }

