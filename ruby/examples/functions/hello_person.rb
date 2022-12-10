def hello_person(name)
  puts "Hello #{name}!"
end

puts "Before"
hello_person "Foo"
hello_person("Bar")
puts "After"
