require "json"

class Person
    include JSON::Serializable

    property name : String
    property height : Float64

    def initialize(@name, @height)
    end
end

prs = Person.new(name: "Jane", height: 173.1)
p! prs
p! prs.to_json


george_str = %{{"name": "George", "height": 171.19}}
#details = JSON.parse(george_str)
#puts details

prs = Person.from_json(george_str)
p! prs
puts prs.name
puts prs.height
puts typeof(prs.name)
puts typeof(prs.height)


people_str = %{[{"name": "George", "height": 171.19}, {"name": "Jane", "height": 168.23}]}
# details = JSON.parse(people_str)
people = Array(Person).from_json(people_str)
p! people

