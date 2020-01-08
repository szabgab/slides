class Person():
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name

x = Person('Joe')
print(x.show())      # Joe

def patch(class_name):
    temp = class_name.show
    def debug(*args, **kwargs):
        print("in debug")
        return temp(*args, **kwargs)
    class_name.show = debug

patch(Person)

print(x.show())
     # in debug
     # Joe

