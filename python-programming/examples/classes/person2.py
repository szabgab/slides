class Person():
    name = 'Joe'
    print(f'Hello {name}')

    def show(self):
        print(Person.name)

x = Person()          # Hello Joe
x.show()              # Joe
print(x.name)         # Joe
print(Person.name)    # Joe

Person.name = 'Jane'
print(x.name)         # Jane
print(Person.name)    # Jane
x.show()              # Jane

x.name = 'Hilda'      # creating and setting the instance attribute
print(x.name)         # Hilda
print(Person.name)    # Jane

x.show()              # Jane
