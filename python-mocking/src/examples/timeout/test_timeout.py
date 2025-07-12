from app import MySystem
import time

def test_app(monkeypatch):
     s = MySystem()
     assert not s.is_logged_in()

     assert not s.login('bar', 'secret')
     assert not s.is_logged_in()

     assert s.login('foo', 'secret')
     assert s.is_logged_in()

     now = time.time() + 60*60*24*7 + 1
     monkeypatch.setattr('time.time', lambda : now)

     assert not s.is_logged_in()

