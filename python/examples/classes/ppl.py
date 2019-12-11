# class Person(object):
#    pass

class Person():
    pass

if __name__ == '__main__':
    p = Person()
    print(p)                     # <__main__.Person object at 0x10fd33150>
    print(type(p))               # <class '__main__.Person'>
    print(p.__class__.__name__)  # Person
