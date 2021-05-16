planets = {
    "Mars" => 1,
    "Jupyter" => 2, 
    "Saturn" => 3,
    "Earth" => 4,
}
puts planets
puts planets.size

planets["Pluto"] = 7

puts planets.each_key {|name|
    puts "#{name}: #{planets[name]}"
}

puts planets.has_key?("Pluto")
puts planets.has_key?("Moon")
