import app
import re

def test_main_page():
    aut = app.app.test_client()

    rv = aut.get('/')
    assert rv.status == '200 OK'
    assert '<form' in str(rv.data)
    assert not 'Welcome back!' in str(rv.data)


def test_verification(monkeypatch):
    aut = app.app.test_client()

    email = 'foo@example.com'

    messages = []
    monkeypatch.setattr('app.sendmail', lambda params: messages.append(params) )

    rv = aut.post('/register', data=dict(email = email ))
    assert rv.status == '200 OK'
    assert 'OK' in str(rv.data)
    print(messages)
    # [{'to': 'foo@example.com', 'subject': 'Registration', 'html': '<a href="/verify/python@example.com/0.81280014">here</a>'}]

    # Remove the html part that we will verify and use later
    html = messages[0].pop('html')

    # Check that the rest of the email is correct
    assert messages == [{'to': 'foo@example.com', 'subject': 'Registration'}]

    # This is the code that we would have received in the email:
    match = re.search(r'/(\d\.\d+)"', html)
    if match:
        code = match.group(1)
    print(code)

    # After the successful verification another email is sent.
    messages = []
    rv = aut.get('/verify/{email}/{code}'.format(email = email, code = code ))
    assert rv.status == '200 OK'
    assert 'OK' in str(rv.data)

    assert messages == [{'to': email, 'subject': 'Welcome!', 'html': ''}]

def test_invalid_verification(monkeypatch):
    aut = app.app.test_client()

    email = 'bar@example.com'

    messages = []
    monkeypatch.setattr('app.sendmail', lambda params: messages.append(params) )

    rv = aut.post('/register', data=dict(email = email ))
    assert rv.status == '200 OK'
    assert 'OK' in str(rv.data)

    messages = []
    # Test what happens if we use an incorrect code to verify the email address:
    rv = aut.get('/verify/{email}/{code}'.format(email = email, code = 'other' ))
    assert rv.status == '200 OK'
    assert 'FAILED' in str(rv.data)

    # No email was sent
    assert messages == []
