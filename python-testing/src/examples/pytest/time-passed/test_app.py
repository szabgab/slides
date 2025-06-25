import app
import time


def test_app(monkeypatch):
    user = app.App()
    user.login('foo')
    assert user.access_page('foo') == 'approved'
    current = time.time()
    print(current)

    monkeypatch.setattr(app.time, 'time', lambda : current + 9)
    assert user.access_page('foo') == 'approved'

    monkeypatch.setattr(app.time, 'time', lambda : current + 11)
    assert user.access_page('foo') == 'expired'

