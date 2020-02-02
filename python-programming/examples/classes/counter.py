class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        #Person.count += 1
        #self.count += 1
        self.count = self.count + 1


print(Person.count)
joe = Person("Joe")
print(Person.count)
print(joe.count)

jane = Person("Jane")
print(Person.count)
print(jane.count)

