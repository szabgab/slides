import time

class App():
    session_length = 10

    def login(self, username):
        self.username = username
        self.start = time.time()

    def access_page(self, username):
        if self.username == username and self.start + self.session_length > time.time():
            return 'approved'
        else:
            return 'expired'

