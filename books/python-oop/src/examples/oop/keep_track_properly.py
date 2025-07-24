import weakref

def prt():
    print(list(Thing.things.keys()))

class Thing:
    things = {}
    def __init__(self):
        Thing.things[id(self)] = weakref.ref(self)

    def __del__(self):
        print('__del__')
        del(Thing.things[id(self)])


def main():
    prt()
    t1 = Thing()
    prt()
    t2 = Thing()
    prt()
    t3 = Thing()
    prt()
    t3 = None
    prt()

main()
prt()

