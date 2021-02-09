import app
import time


def test_app():
    user = app.App()
    user.login('foo')
    assert user.access_page('foo') == 'approved'
    current = time.time()
    print(current)

    app.time.time = lambda : current + 9
    assert user.access_page('foo') == 'approved'

    app.time.time = lambda : current + 11
    assert user.access_page('foo') == 'expired'

