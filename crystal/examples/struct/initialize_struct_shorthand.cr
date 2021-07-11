struct Person
  def initialize(@name : String, @email : String)
    @time = Time.utc
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
