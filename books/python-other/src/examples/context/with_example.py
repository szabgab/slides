class WithClass:
    def __init__(self, name='default'):
        self.name = name

    def __enter__(self):
        print('entering the system')
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        print('exiting the system')

    def __str__(self):
        return 'WithObject:'+self.name

x = WithClass()
with x as y:
    print(x,y)

