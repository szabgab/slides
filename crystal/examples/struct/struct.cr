struct Person
  property name : String
  property email : String

  def initialize(@name, @email)
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
