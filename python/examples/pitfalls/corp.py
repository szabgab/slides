
class Corp(object):
    people = []
    def add(self, name, salary):
        Corp.people.append({ 'name': name, 'salary' : salary})

    def total(self):
        self.total = 0
        for n in Corp.people:
            self.total += n['salary']
        return self.total

c = Corp()
c.add("Foo", 19)
print(c.total())

c.add("Bar", 23)
print(c.total())
