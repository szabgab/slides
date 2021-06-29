class Person
  def initialize(name : String, height : Float64)
    @name = name
    @height = height
  end

  def name
    @name
  end
end

prs = Person.new(name: "Joe", height: 180)
puts prs      # #<Person:0x7f1678dd0e40>
p! prs        # prs # => #<Person:0x7f1678dd0e40 @name="Joe", @height=180.0>
puts prs.name # Joe

# prs.name = "Jane"
# Error: undefined method 'name=' for Person
