things_str = %{["table", "chair"]}
data = JSON.parse(things_str)
p! data

# data.each {|thing|
#     puts thing
# }
# Error: undefined method 'each' for JSON::Any

things = Array(String).from_json(things_str)
p! things

things.each { |thing|
  puts thing
}
