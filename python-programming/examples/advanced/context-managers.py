class CM(object):
    def __init__(self, n):
        self.name = n

    def __enter__(self):
        print('__enter__', self.name)

    def __exit__(self, exception_type, exception, traceback):
        print('__exit__ ', self.name)

    def something(self):
        print('something', self.name)

def main():
    a = CM('a')
    b = CM('b')
    with a, b:
        a.partner = b
        b.partner = a
        a.something()
        raise Exception('nono')
        b.something()
    print('in main - after')

main()
print('after main')
