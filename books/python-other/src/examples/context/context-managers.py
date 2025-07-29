class MyCM:
    def __init__(self, n):
        self.name = n

    def __enter__(self):
        print('__enter__', self.name)

    def __exit__(self, exception_type, exception, traceback):
        print('__exit__ ', self.name)

    def something(self):
        print('something', self.name)

def main():
    a = MyCM('a')
    b = MyCM('b')
    with a, b:
        a.partner = b
        b.partner = a
        a.something()
        raise Exception('nono')
        b.something()
    print('in main - after')

main()
print('after main')
