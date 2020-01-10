class Person():
    name = 'Original'
    print(f'Hello {name}')

    def show(self):
        print(Person.name)

print(Person.name)    # Original

Person.name = 'Joe'
print(Person.name)    # Joe

x = Person()
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
