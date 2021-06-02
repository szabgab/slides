class Person
    property name : String

    def initialize(name)
        @name = name
    end
end

prs = Person.new(name: "Joe")
p! prs             # prs # => #<Person:0x7f8d0f266e80 @name="Joe">
puts prs.name      # Joe
prs.name = "Jane"
puts prs.name      # Jane
