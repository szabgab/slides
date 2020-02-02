class App:
    def __init__(self):
        self.pi = 3.14
        # .. set up database
        print("__init__ of App")


    def shutdown(self):
        print("shutdown of App cleaning up database")


    def add_user(self, name):
        print("Working on add_user({})".format(name))
