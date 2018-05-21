def calc():
    a = input("Type in a: ")
    b = input("Type in b: ")

    print("The result is:", add(int(a), int(b)))

def add(x, y):
    return x+y

if __name__ == '__main__':
    calc()
