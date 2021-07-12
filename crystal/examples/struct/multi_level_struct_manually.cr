require "json"

struct Address
  getter street : String
  getter city : String
  getter country : String

  def initialize(@street, @city, @country)
  end
end

struct Person
  getter name : String
  getter email : String
  getter address : Address

  def initialize(@name, @email, @address)
  end
end

adr = Address.new("Main str. 3", "Capital", "Big")
p! adr

prs = Person.new("Foo", "me@foo.bar", adr)
p! prs
