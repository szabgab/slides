from hidden import Thing

t = Thing()
#print(t.__hidden)  # AttributeError: 'Thing' object has no attribute '__hidden'

print(t.get_hidden())    # lake

print(dir(t))            # ['_Thing__hidden',  ...]

print(t._Thing__hidden)  # lake

t._Thing__hidden = 'Not any more'
print(t._Thing__hidden)  # Not any more

