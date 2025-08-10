struct Person
  getter first : String
  getter family : String?

  def initialize(@first)
  end

  def initialize(@first, @family)
  end
end

if Random.rand < 0.5
  prs = Person.new("Foo")
else
  prs = Person.new("Foo", "Bar")
end

if prs.family.nil?
  puts "nil"
else
  puts "not nil"
  puts prs.family.size
end
