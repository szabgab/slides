require "json"

data = {
    "Mars" => 1,
    "Jupyter" => 2,
    "Saturn" => 3,
    "Earth" => 4,
    "moons" => ["Our", "Jupyters"],
    "missing" => nil
}
puts data   # Hash(String, Array(String) | Int32 | Nil)
json_string = data.to_json
puts json_string

parsed = JSON.parse(json_string)
puts parsed  # JSON::Any

other = Hash(String, Array(String) | Int32 | Nil).from_json(json_string)
puts other.keys()


