name = "Foo"
person = {
  name:    "Foo",
  number:  42,
  yesno:   true,
  fruits:  ["apple", "banana", "peach"],
  address: {
    "street"  => "Main str.",
    "city"    => "Capital",
    "country" => "Country",
  },
}
puts name
p name
p! name
pp! name

puts ""

puts person
p person
p! person
pp! person
