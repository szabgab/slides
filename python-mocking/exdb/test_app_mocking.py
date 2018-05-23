import db
import os
from bank import Bank

class MockDB(object):
    def create(self):
        self.db = {}

    def status(self, name):
        return self.db.get(name)

    def deposit(self, name, amount):
        if name not in self.db:
            self.db[name] = 0
        self.db[name] += amount


db.DB = MockDB

def test_app(tmpdir):
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


