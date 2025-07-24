class Person():
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

y = Person('Jane')
print(y.name)    # Jane
y.show()         # Jane

def new_show(some_instance):
    print("Hello " + some_instance.name)

Person.show = new_show
y.show()         # Hello Jane
