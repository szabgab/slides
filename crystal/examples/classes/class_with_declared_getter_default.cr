class Person
    getter name : String

    def initialize()
        @name = "Default name"
    end
end

prs = Person.new
p! prs         # prs # => #<Person:0x7f804672fe80 @name="Default name">
puts prs.name  # Default name

# prs.name = "Joe"
# Error: undefined method 'name=' for Person
