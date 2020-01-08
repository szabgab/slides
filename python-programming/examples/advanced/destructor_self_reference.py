class Destruct(object):
    def __init__(self, name):
        self.name = name
        print('__init__')
    def __del__(self):
        print(f'__del__ {self.name}')

def main():
    a = Destruct('A')
    b = Destruct('B')
    a.partner = a
    print('in main - after')

main()
print('after main')

