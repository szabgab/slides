class Person():
    def __init__(self, name):
        self.name = name

y = Person('Jane')
print(y.name)           # Jane

def show(some_instance):
    print("Hello " + some_instance.name)

Person.show = show
y.show()                # Hello Jane
