class ParentA:
    def __init__(self):
        print('__init__ of ParentA')

    def in_parent_a(self):
        print('in_parent_a')

    def in_both(self):
        print('in_both in parent A')

class ParentB:
    def __init__(self):
        print('__init__ of ParentB')

    def in_parent_b(self):
        print('in_parent_b')

    def in_both(self):
        print('in_both in paernt B')

class Child(ParentA, ParentB):
    def __init__(self):
        print('__init__ of Child')
        super().__init__()

    def in_child(self):
        print('in_child')

c = Child()
c.in_parent_a()
c.in_parent_b()
c.in_child()
c.in_both()

