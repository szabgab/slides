struct Person
  def initialize(@name : String, @email : String)
  end

  def name
    @name
  end

  def email
    @email
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
p! foo.name
p! foo.email
