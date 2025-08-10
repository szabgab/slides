phone_of = {} of String => String | Int32
phone_of["Jane"] = "123"
phone_of["Jack"] = "456"

phone_of["Narnia"] = 42

# phone_of["is_it_true?"] = true
# Error: no overload matches 'Hash(String, Int32 | String)#[]=' with types String, Bool

puts phone_of
