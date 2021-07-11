require "json"

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String
end

json_str = %{{"name": "Bar", "email": "bar@foobar.com"}}
bar = Person.from_json(json_str)
p! bar
