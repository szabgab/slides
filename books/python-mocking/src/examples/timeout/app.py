import time

TIMEOUT = 60*60*24*7

class MySystem():
    def __init__(self):
        self.logged_in = 0

    def login(self, name, password):
        resp = self.verify_user(name, password)
        if resp:
            self.logged_in = True
            self.seen()

        return resp

    def seen(self):
        self.last_seen = time.time()

    def is_logged_in(self):
        return self.logged_in and self.last_seen + TIMEOUT > time.time()

    def verify_user(self, name, password):
        if name == 'foo' and password == 'secret':
            return True
        return False
