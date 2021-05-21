require "yaml"

data = File.open("examples/crystal.yml") do |file|
    YAML.parse(file)
end
puts data
puts data["language"]