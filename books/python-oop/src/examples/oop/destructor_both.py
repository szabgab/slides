class Thing:
    def __init__(self, name):
        self.name = name
        print(f'__init__ for {self.name}')
    def __del__(self):
        print(f'__del__ for {self.name}')

def main():
    a = Thing('A')
    b = Thing('B')
    a.partner = b
    b.partner = a
    print('in main - after')

main()
print('after main')

