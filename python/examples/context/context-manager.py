class MyCM:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'__enter__ {self.name}')
        return self

    def __exit__(self, exception_type, exception, traceback):
        print(f'__exit__  {self.name}')

    def something(self):
        print(f'something {self.name}')

def main():
    with MyCM('Foo') as cm:
        print(cm.name)
        cm.something()
        #raise Exception('nono')
    print('in main - after')

main()
print('after main')
