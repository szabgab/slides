struct Person
  getter name, email

  def initialize(@name : String, @email : String)
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
p! foo.name
p! foo.email
