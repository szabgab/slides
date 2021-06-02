class Person
    property name : String

    def initialize()
        @name = "Default name"
    end
end

prs = Person.new
p! prs           # prs # => #<Person:0x7fa3aaae2eb0>
puts prs.name    # Default name
prs.name = "Joe"
puts prs.name    # joe
