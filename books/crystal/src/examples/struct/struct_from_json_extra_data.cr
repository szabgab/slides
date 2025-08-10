require "json"

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String
end

json_str = %[{
  "name": "Bar",
  "email": "bar@foobar.com",
  "address" : "Somewhere"
}]
prs = Person.from_json(json_str)
pp! prs

p! prs.name
