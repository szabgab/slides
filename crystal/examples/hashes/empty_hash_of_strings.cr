phone_of = {} of String => String
phone_of["Jane"] = "123"
phone_of["Jack"] = "456"

# phone_of["Narnia"] = 42
# Error: no overload matches 'Hash(String, String)#[]=' with types String, Int32

puts phone_of
