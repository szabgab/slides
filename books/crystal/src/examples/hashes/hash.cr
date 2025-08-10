planets = {
  "Mars"    => 1,
  "Jupyter" => 2,
  "Saturn"  => 3,
  "Earth"   => 4,
}
puts planets
puts planets.size
puts planets.keys

planets["Pluto"] = 7

puts planets.each_key { |name|
  puts "#{name}: #{planets[name]}"
}

puts planets.has_key?("Pluto") # true
puts planets.has_key?("Moon")  # false

puts planets.has_value?(3) # true
puts planets.has_value?(8) # false
