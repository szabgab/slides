import pickle

class aClass(object):
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name


the_instance = aClass(42, "FooBar")

a = {
    "name": "Some Name",
    "address" : ['country', 'city', 'street'],
    'repr' : the_instance,
}

print(a)

pickle_string = pickle.dumps(a)

b = pickle.loads(pickle_string)

print(b)

print(b['repr'].amount)
print(b['repr'].name)

