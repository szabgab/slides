require "json"

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String
  getter address : String?
end

json_str = %[{
  "name": "Bar",
  "email": "bar@foobar.com",
  "address" : "my address"
}]
prs = Person.from_json(json_str)
pp! prs
p! prs.name
p! prs.address
puts ""

json_str = %[{
  "name": "Bar",
  "email": "bar@foobar.com"
}]
prs = Person.from_json(json_str)
pp! prs
p! prs.name
p! prs.address
