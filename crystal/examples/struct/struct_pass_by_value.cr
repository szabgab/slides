struct Person
  property name : String
  property email : String

  def initialize(@name, @email)
  end
end

def set_email(prs : Person)
  prs.email = "fake@address.com"
end

foo = Person.new("Foo", "me@foo.bar")
p! foo
p! foo.name
p! foo.email

set_email(foo)

p! foo.email
