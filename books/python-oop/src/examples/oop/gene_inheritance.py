import random

class Person(object):
    def __init__(self, DNA):
        self.DNA = DNA

    def gene(self):
        return list(self.DNA)

    def print_genes(self):
        print(list(self.DNA))

    def __add__(self, other):
        DNA_father = self.gene()
        DNA_mother = other.gene()
        if len(DNA_father) != len(DNA_mother):
            raise Exception("Incompatible couple")

        DNA_childPosible_sequence = DNA_father + DNA_mother
        DNA_child = ""
        for i in range(len(self.gene())):
            DNA_child += random.choice([DNA_father[i], DNA_mother[i]])

        return Person(DNA_child)


a = Person("ABCD")
b = Person("1234")
c = a + b
print(c.DNA)

