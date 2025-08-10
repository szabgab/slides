names = ["Foo", "Bar"]
puts names.first # Foo
puts names[0]    # Foo

names = [] of String
# puts names.first
# Unhandled exception: Empty enumerable (Enumerable::EmptyError)

# puts names[0]
# Unhandled exception: Index out of bounds (IndexError)

first = names.first?
puts first.nil? # true
first = names[0]?
puts first.nil? # true
