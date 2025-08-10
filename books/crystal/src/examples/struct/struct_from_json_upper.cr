require "json"

struct Person
  include JSON::Serializable

  getter name : String

  @[JSON::Field(key: "Email")]
  getter email : String
end

json_str = %{{"name": "Bar", "Email": "bar@foobar.com"}}
prs = Person.from_json(json_str)
p! prs
p! prs.name
p! prs.email
