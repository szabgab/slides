require "yaml"

data = File.open("examples/crystal.yml") do |file|
    YAML.parse(file)
end
puts data
puts typeof(data) # YAML::Any
puts data["language"]
puts data["language"]["first_year"]
puts typeof(data["language"]["first_year"].to_s.to_i)
# [YAML::Any](https://crystal-lang.org/api/YAML/Any.html)
puts data.as_h.keys
data.as_h.keys.each {|main_key|
    data[main_key].as_h.keys.each {|sub_key|
        puts data[main_key][sub_key]
    }
}