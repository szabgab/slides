require "json"

struct Address
  include JSON::Serializable

  getter street : String
  getter city : String
  getter country : String

  def initialize(@street, @city, @country)
  end
end

struct Person
  include JSON::Serializable

  getter name : String
  getter email : String
  getter address : Address

  def initialize(@name, @email, @address)
  end
end

adr = Address.new("Main str. 3", "Capital", "Big")
p! adr

foo = Person.new("Foo", "me@foo.bar", adr)
p! foo

json_str = %{{"name": "Bar", "email": "bar@foobar.com", "address" : { "street": "Broadway", "city": "New York", "country": "USA"} }}
bar = Person.from_json(json_str)
p! bar

p bar.name
p bar.address
p bar.address.street
