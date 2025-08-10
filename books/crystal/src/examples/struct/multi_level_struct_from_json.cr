require "json"

struct Address
  include JSON::Serializable

  getter street : String
  getter city : String
  getter country : String
end

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String
  getter address : Address
end

json_str = %[{
  "name": "Bar",
  "email": "bar@foobar.com",
  "address" : {
    "street": "Broadway",
    "city": "New York",
    "country": "USA"
   }
}]
prs = Person.from_json(json_str)
pp! prs

p! prs.name
p! prs.address
p! prs.address.street
