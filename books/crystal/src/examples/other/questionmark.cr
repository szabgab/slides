[0, 23, nil].each { |value|
  puts value.nil?
  z = value || 42
  puts z
}

names = ["Foo", "Bar"]
puts names[1]

# puts names[2]
# Unhandled exception: Index out of bounds (IndexError)

z = names[2]? # nil
puts z.nil?   # true

person = {
  "name"  => "Foo",
  "email" => "foo@bar.com",
}
puts person
puts person["name"]
# puts person["age"]
# Unhandled exception: Missing hash key: "age" (KeyError)
z = person["age"]?
puts z.nil? # true
