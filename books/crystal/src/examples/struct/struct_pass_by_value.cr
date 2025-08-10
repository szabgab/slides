struct Person
  property name : String
  property email : String

  def initialize(@name, @email)
  end
end

def set_email(pers : Person)
  pers.email = "fake@address.com"
  p! pers
end

prs = Person.new("Foo", "me@foo.bar")
p! prs
p! prs.name
p! prs.email

puts ""

set_email(prs)

puts ""
p! prs
p! prs.name
p! prs.email
