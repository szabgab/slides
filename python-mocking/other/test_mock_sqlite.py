from db import DB
import sqlite3

def test_pass():
    pass

#class MockSQLiteCursor(object):
#    def execute(self, sql):
#        pass
#
#class MockSQLiteConnection(object):
#    def cursor(self):
#        return MockSQLiteCursor()
#
#def connect(filename):
#    return MockSQLiteConnection()
#
#sqlite3.connect = connect
#
#def test_db():
#    db = DB('hello.db')
#    db.create()
#    assert db.status('foo') == None
#    assert db.status('bar') == None
#
#    db.deposit('foo', 100)
#    assert db.status('foo') == 100
#
#    db.deposit('foo', 10)
#    assert db.status('foo') == 110
#
#    db.deposit('bar', 130)
#    assert db.status('foo') == 110
#    assert db.status('bar') == 130
#
#    db.transfer('foo', 'bar', 19)
#    assert db.status('foo') == 91
#    assert db.status('bar') == 149

