struct Person
  def initialize(@name : String, @email : String)
  end

  def name
    @name
  end

  def email
    @email
  end

  def name(value)
    @name = value
  end

  def email=(value)
    @email = value
  end
end

prs = Person.new("Foo", "me@foo.bar")
p! prs
p! prs.name
p! prs.email

prs.name("Bar")
p! prs.name

prs.email=("bar@foo.bar")
p! prs.email

prs.email = "new@foo.bar"
p! prs.email
