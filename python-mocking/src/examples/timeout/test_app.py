from app import MySystem

def test_app():
     s = MySystem()
     assert not s.is_logged_in()

     assert not s.login('bar', 'secret')
     assert not s.is_logged_in()

     assert s.login('foo', 'secret')
     assert s.is_logged_in()

     # how to test the timeout?
