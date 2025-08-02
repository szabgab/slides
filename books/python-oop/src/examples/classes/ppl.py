class Person:
    pass

if __name__ == '__main__':
    p = Person()
    print(p)
    print(type(p))
    print(p.__class__.__name__)

    members = dir(p)
    print(members)
