require "json"

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String

  def initialize(@name, @email)
  end
end

prs1 = Person.new("Foo", "me@foo.bar")
p! prs1
p! prs1.name
p! prs1.email

json_str = %{{"name": "Bar", "email": "bar@foobar.com"}}
prs2 = Person.from_json(json_str)
p! prs2
p! prs2.name
p! prs2.email
