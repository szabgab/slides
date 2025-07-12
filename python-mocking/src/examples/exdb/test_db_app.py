import os
import pytest

import db
from bank import Bank


def test_app(tmpdir):
    db.db_filename = os.path.join( tmpdir, 'test.db' )
    app = Bank()
    app.setup()
    assert app.status('foo') == None
    assert app.status('bar') == None

    app.deposit('foo', 100)
    assert app.status('foo') == 100

    app.deposit('foo', 10)
    assert app.status('foo') == 110

    app.deposit('bar', 130)
    assert app.status('foo') == 110
    assert app.status('bar') == 130

    app.transfer('foo', 'bar', 19)
    assert app.status('foo') == 91
    assert app.status('bar') == 149

    with pytest.raises(Exception) as exinfo:
        app.transfer('foo', 'bar', 200)
    assert exinfo.type == Exception
    assert str(exinfo.value) == 'Not enough money' 
