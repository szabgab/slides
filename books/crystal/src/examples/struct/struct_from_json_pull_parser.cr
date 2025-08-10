require "json"

struct Person
  getter name : String
  getter email : String

  def initialize(pull) # JSON::PullParser
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

json_str = %{{"name": "Bar", "email": "bar@foobar.com"}}
prs = Person.from_json(json_str)
p! prs
p! prs.name
p! prs.email
