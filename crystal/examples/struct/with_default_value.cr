struct Person
  property name : String = ""
  property email : String?
end

prs = Person.new
p! prs
p! prs.name
p! prs.email

prs.name = "Foo"
prs.email = "new@foo.bar"
p! prs.name
p! prs.email
