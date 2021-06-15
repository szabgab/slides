#:pi = 3.14
values = {
    "foo" => 1,
    "bar" => 2,
    "baz" => 3,
}

#puts :pi
names = %i(foo bar baz)
puts names
puts names[0]
puts typeof(names)
puts typeof(names[0])

puts values
#names.each {|name|
#    puts name
#    values[name]
#}
