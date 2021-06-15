h = {
    "fname" => "Foo",
}



# g and i are the same 
i = {
    :fname => "Foo"
}

g = {
    fname: "Foo", # Symbol
}

puts h
puts typeof(h)
h["lname"] = "Bar"
puts h
# puts h[:lname]
# Missing hash key: :lname (KeyError)



# joe = {} of String => Int32 | String
# joe["name"] = "Joe"
# joe["number"] = 23
# # joe["float"] = 2.3
# # compile time error
# # Error: no overload matches 'Hash(String, Int32 | String)#[]=' with types String, Float64
# puts typeof(joe)


# #alias Some = {} of String => Int32 | String

# numbers = [] of Int32
# numbers.push(23)
# # numbers.push("text")
# # Error: no overload matches 'Array(Int32)#push' with type String
# # numbers.push(nil)
# # Error: no overload matches 'Array(Int32)#push' with type Nil
# puts typeof(numbers)

# alias Int32orNil = Int32|Nil
# # nilnum = [] of Int32 | Nil
# nilnum = [] of Int32orNil
# nilnum.push(23)
# nilnum.push(nil)
# puts typeof(nilnum)
# #num = Int32
# #num = 23
# #num = nil

# # class Person
# #     name: {type: String}
# #     number: {type: Int32}
# # end

# #alias Person = {name: String, number: Int32}
# alias Person = NamedTuple(name: String, number: Int32)

# people = [] of Person
# puts typeof(people)
# people.push({
#     "name": "Foo Bar",
#     "number": 42
# })

# puts people[0]["name"]
# # people[0]["name"] = "New Name"
# # Error: undefined method '[]=' for NamedTuple(name: String, number: Int32)
