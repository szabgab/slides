class Person
  def initialize(name : String, height : Float64)
    @name = name
    @height = height
  end
end

# prs = Person.new
# Error: wrong number of arguments for 'Person.new' (given 0, expected 2)

prs = Person.new(name: "Joe", height: 180)
puts prs # #<Person:0x7f3e27f68e40>
p! prs   # prs # => #<Person:0x7f3e27f68e40 @name="Joe", @height=180.0>

# puts prs.name
# Error: undefined method 'name' for Person
