import app
import re

def test_app(monkeypatch):
    aut = app.app.test_client()

    rv = aut.get('/')
    assert rv.status == '200 OK'
    assert '<form' in str(rv.data)
    assert not 'Welcome back!' in str(rv.data)

    email = 'foo@bar.com'

    messages = []
    monkeypatch.setattr('app.sendmail', lambda params: messages.append(params) )

    rv = aut.post('/register', data=dict(email = email ))
    assert rv.status == '200 OK'
    assert 'OK' in str(rv.data)
    print(messages)
    # [{'to': 'foo@bar.com', 'subject': 'Registration', 'html': '<a href="/verify/foo@bar.com/0.81280014">here</a>'}]

    rv = aut.get('/verify/{email}/{code}'.format(email = email, code = 'other' ))
    assert rv.status == '200 OK'
    assert 'FAILED' in str(rv.data)

    match = re.search(r'/(\d\.\d+)"', messages[0]['html'])
    if match:
        code = match.group(1)
    print(code)

    messages = []
    rv = aut.get('/verify/{email}/{code}'.format(email = email, code = code ))
    assert rv.status == '200 OK'
    assert 'OK' in str(rv.data)

    assert messages == [{'to': email, 'subject': 'Welcome!', 'html': ''}]


