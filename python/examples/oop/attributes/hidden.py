class Thing:
    def __init__(self):
        self.__hidden = 'lake'

    def get_hidden(self):
        return self.__hidden

t = Thing()

#print(t.__hidden)  # AttributeError: 'Thing' object has no attribute '__hidden'
print(t.get_hidden())    # lake

print(dir(t))            # ['_Thing__hidden',  ...]

print(t._Thing__hidden)  # lake

t._Thing__hidden = 'Not any more'
print(t._Thing__hidden)  # Not any more


class SubThing(Thing):
    def __init__(self):
        super().__init__()
        self.__hidden = 'river'

    def get_sub_hidden(self):
        return self.__hidden

st = SubThing()
print(dir(st))
print(st._Thing__hidden)
print(st._SubThing__hidden)


print(st.get_hidden())
print(st.get_sub_hidden())
