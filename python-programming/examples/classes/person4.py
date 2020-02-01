class Person():
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name

y = Person('Jane')
print(y.show())         # Jane

def new_show(some_instance):
    print("Hello " + some_instance.name)
    return some_instance

Person.show = new_show
y.show()                # Hello Jane
