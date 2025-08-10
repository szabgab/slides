a = {fname: "Foo", "lname": "Bar"}
puts a
puts typeof(a)

b = NamedTuple.new(fname: "Foo", "lname": "Bar")
puts b
puts typeof(b)
