class Thing:
    def __init__(self, name):
        self.name = name
        print(f'__init__ {name}')

    def __del__(self):
        print(f'__del__ {self.name}')

def main():
    a = Thing('A')
    b = Thing('B')
    a.partner = a
    print('in main - after')

main()
print('after main')

