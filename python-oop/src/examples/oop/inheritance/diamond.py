class GrandParent:
    ...

class ParentA(GrandParent):
    ...

class ParentB(GrandParent):
    ...

class Child(ParentA, ParentB):
    ...

c = Child()

