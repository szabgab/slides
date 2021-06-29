require "./person"

class Person
  property email : String | ::Nil
end

prs = Person.new(name: "Joe", height: 180)
puts prs # #<Person:0x7f3e27f68e40>
p! prs   # prs # => #<Person:0x7f3e27f68e40 @name="Joe", @email=nil, @height=180.0>

prs.email = "foo@bar.com"
p! prs # prs # => #<Person:0x7f3e27f68e40 @name="Joe", @email="foo@bar.com", @height=180.0>
