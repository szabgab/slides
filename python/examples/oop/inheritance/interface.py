class Parent:
    def __init__(self):
        print('__init__ of Parent')

    def in_parent(self):
        print('in_parent')

class Tools:
    def some_tool(self):
        print('some_tool')

class Child(Parent, Tools):
    def __init__(self):
        print('__init__ of Child')
        super().__init__()

    def in_child(self):
        print('in_child')

c = Child()
c.in_parent()
c.some_tool()
c.in_child()

