class Parent:
    def __init__(self):
        print('__init__ of Parent')

    def in_parent(self):
        print('in_parent')

    def in_both(self):
        print('both in parent')

class Other:
    def in_other(self):
        print('in_other')

    def in_both(self):
        print('both in other')

class Child(Parent, Other):
    def __init__(self):
        print('__init__ of Child')
        super().__init__()

    def in_child(self):
        print('in_child')

c = Child()
c.in_parent()
c.in_other()
c.in_child()

c.in_both()

# __init__ of Parent
# in_parent
# in_other
# in_child
# both in parent



