class Person():
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name

x = Person('Joe')
y = Person('Jane')
print(x.show())         # Joe
print(y.show())         # Jane

def new_show(some_instance):
    print("Hello " + some_instance.name)
    return some_instance

Person.show = new_show
x.show()             # Hello Joe
y.show()             # Hello Jane
