require "json"

struct Address
  include JSON::Serializable

  property street : String
  property city : String
  property country : String

  def initialize(@street, @city, @country)
  end
end

struct Person
  include JSON::Serializable

  property name : String
  property email : String
  property address : Address

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
