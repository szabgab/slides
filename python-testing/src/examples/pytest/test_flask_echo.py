import flask_echo

class TestEcho:
    def setup_method(self):
        self.app = flask_echo.eapp.test_client()
        print("setup")

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'<form action="/echo" method="GET">' in rv.data

    def test_echo(self):
        rv = self.app.get('/echo?text=Hello')
        assert rv.status == '200 OK'
        assert b'You said: Hello' in rv.data

    def test_empty_echo(self):
        rv = self.app.get('/echo')
        assert rv.status == '200 OK'
        assert b'Nothing to say?' in rv.data
