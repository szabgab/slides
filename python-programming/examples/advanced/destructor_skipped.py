class Person:
    def __init__(self, name):
        self.name = name
        print(f'__init__ for {self.name}')
    def __del__(self):
        print(f'__del__ for {self.name}')

def main():
    a = Person('Joe')
    b = Person('Jane')
    a.partner = b
    b.partner = a
    print('in main - after')

main()
print('after main')

