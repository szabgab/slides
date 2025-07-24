import app
import os

#def test_func():
#   assert app.func(2, 3) == 5


def test_func():
    pid = os.getpid()
    try:
        res = app.func(2, 3)
        assert res == 5
    except SystemExit as ex:
        assert str(ex) == 'None'
        #SystemExit(None)
        # or ex == 0
        if pid == os.getpid():
            raise ex

