require "json"

struct Person
  property name : String
  property email : String

  def initialize(@name, @email)
  end

  def initialize(pull)
    @name = ""
    @email = ""
    pull.read_object do |key|
      case key
      when "name"
        @name = pull.read_string
      when "email"
        @email = pull.read_string
      end
    end
  end
end

foo = Person.new("Foo", "me@foo.bar")
p! foo

json_str = %{{"name": "Bar", "email": "bar@foobar.com"}}
bar = Person.from_json(json_str)
p! bar
