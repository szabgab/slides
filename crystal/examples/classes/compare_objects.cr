class Person
  def_equals @name, @height
  property name : String
  property height : Float64

  def initialize(@name, @height)
  end
end

prs1 = Person.new(name: "Jane", height: 173.1)
prs2 = prs1.dup
prs3 = Person.new(name: "Jane", height: 173.1)
prs4 = prs1
prs5 = Person.new(name: "Jane", height: 173.2)
p! prs1
p! prs2
p! prs3
puts prs1 == prs2 # true
puts prs1 == prs3 # true

puts prs1 == prs4 # true
puts prs1 == prs5 # false
