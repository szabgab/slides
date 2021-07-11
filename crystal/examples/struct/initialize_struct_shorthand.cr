struct Person
  def initialize(@name : String, @email : String)
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
