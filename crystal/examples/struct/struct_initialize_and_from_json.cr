require "json"

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String

  def initialize(@name, @email)
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo

json_str = %{{"name": "Bar", "email": "bar@foobar.com"}}
bar = Person.from_json(json_str)
p! bar
