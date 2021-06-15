require "./person"

class Person
    def name
        return @name
    end
end

prs = Person.new(name: "Joe", height: 180)
puts prs  # #<Person:0x7f3e27f68e40>
p! prs    # prs # => #<Person:0x7f3e27f68e40 @name="Joe", @height=180.0>

puts prs.name

