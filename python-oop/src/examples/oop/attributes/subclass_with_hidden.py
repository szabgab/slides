from hidden import Thing

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
