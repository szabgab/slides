people = {
    "foo" : "123",
    "bar" : "456",
    "qux" : "789",
}

for name, uid in people.items():
    print("{} => {}".format(name, uid))
