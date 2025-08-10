struct Person
  property name : String
  property email : String?

  def initialize(@name)
  end

  def initialize(@name, @email)
  end
end

prs = Person.new("Foo")
p! prs
p! prs.name
p! prs.email

prs.email = "foo@bar.com"
p! prs
p! prs.email
