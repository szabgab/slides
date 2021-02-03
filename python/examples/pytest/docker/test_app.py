import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Post JSON to /api/calc' == rv.data

def test_calc():
    web = app.app.test_client()

    rv = web.get('/api/calc?a=10&b=2')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  10,
        "b"        :  2,
        "add"      :  12,
    }


