class Person
    property name : String

    def initialize(@name = "George")
    end
end

prs = Person.new(name: "Joe")
p! prs             # prs # => #<Person:0x7f8d0f266e80 @name="Joe">
puts prs.name      # Joe
prs.name = "Jane"
puts prs.name      # Jane

defaulty = Person.new()
puts defaulty.name # George
