phone_of = {} of String => String
puts phone_of.empty?

phone_of["Jane"] = "123"
phone_of["Jack"] = "456"

# phone_of["Narnia"] = 42
# Error: no overload matches 'Hash(String, String)#[]=' with types String, Int32

puts phone_of
puts phone_of.empty?
