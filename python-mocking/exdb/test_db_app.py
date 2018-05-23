from db import DB
import os


def test_db(tmpdir):
    filename = os.path.join( tmpdir, 'test.db' )
    db = DB(filename)
    db.create()
    assert db.status('foo') == None



#    db.deposit('foo', 100)
#    assert db.status('foo') == 100
#
#    db.deposit('bar', 130)
#    assert db.status('foo') == 100
#    assert db.status('bar') == 130

