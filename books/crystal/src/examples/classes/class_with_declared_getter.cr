class Person
  getter name : String

  def initialize(name)
    @name = name
  end
end

prs = Person.new(name: "Joe")
p! prs        # prs # => #<Person:0x7f804672fe80 @name="Joe">
puts prs.name # Joe

# prs.name = "Jane"
# Error: undefined method 'name=' for Person
