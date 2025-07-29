class Person(object):
    def __init__(self, name):
        print(f"init:            '{self}'   '{self.__class__.__name__}'")
        self.name = name

    def show_name(self):
        print(f"instance method: '{self}'   '{self.__class__.__name__}'")

    @classmethod
    def from_occupation(cls, occupation):
        print(f"class method     '{cls}'    '{cls.__class__.__name__}'")

    @staticmethod
    def is_valid_occupation(param):
        print(f"static method   '{param}'    '{param.__class__.__name__}'")


fb = Person('Foo Bar')
fb.show_name()

fb.from_occupation('Tailor')
Person.from_occupation('Tailor') # This is how we should call it.

fb.is_valid_occupation('Tailor')
Person.is_valid_occupation('Tailor')
