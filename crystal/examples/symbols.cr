# :pi = 3.14
values = {
  "foo" => 1,
  "bar" => 2,
  "baz" => 3,
}

# puts :pi
names = %i(foo bar baz)
puts names
puts names[0]
puts typeof(names)
puts typeof(names[0])

puts values
# names.each {|name|
#    puts name
#    values[name]
# }

h = {
  "fname" => "Foo",
}
puts h
puts typeof(h)
h["lname"] = "Bar"
puts h
# puts h[:lname]
# Missing hash key: :lname (KeyError)

# g and i are the same
i = {
  :fname => "Foo",
}
puts i
puts typeof(i)
# i["fname"]
puts i[:fname]

g = {
  fname: "Foo", # Symbol
}
puts g[:fname]
