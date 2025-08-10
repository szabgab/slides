require "json"

alias Constant = NamedTuple(name: String, value: Float64)
alias MathResponseType = NamedTuple(
  status: Int32,
  status_text: String,
  count: Int32,
  results: Array(Constant))
main

def main
  if ARGV.size != 1
    puts "Needs filename eg. math.json"
    exit 1
  end
  filename = ARGV[0]
  content = File.read(filename)
  data = MathResponseType.from_json(content)
  puts data
  puts data["results"][0].keys
end

# This will complain if field is missing or the value of a field is of incorrect type,
# but it will silently ignore any extra fields
