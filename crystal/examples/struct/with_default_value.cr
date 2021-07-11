struct Person
  property name : String = ""
  property email : String?
end

foo = Person.new
p! foo
p! foo.name
p! foo.email

foo.email = "new@foo.bar"
p! foo.email
