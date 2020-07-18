class Person:
    def __init__(self):
        print('__init__')
    def __del__(self):
        print('__del__')

def main():
    a = Person()
    print('in main - after')

main()
print('after main')


