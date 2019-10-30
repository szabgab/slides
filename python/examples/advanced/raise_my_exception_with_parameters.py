class MyError(Exception):
    def __init__(self, first, second):
        self.first  = first
        self.second = second
    def __str__(self):
        return 'Problems? {} and {}'.format(self.first, self.second)

try:
    raise(MyError('hello', 'world'))
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)

    print(e.first)
    print(e.second)

