class Thing:
    def __init__(self):
        self.__secret = 'Sick Rat'

    def get_secret(self):
        return self.__secret

t = Thing()

#print(t.__secret)  # AttributeError: 'Thing' object has no attribute '__secret'
print(t.get_secret())    # Sick Rat


print(t._Thing__secret)  # Sick Rat
