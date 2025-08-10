planets = {
  "Mars"    => 1,
  "Jupyter" => 2,
  "Saturn"  => 3,
  "Earth"   => 4,
}

puts planets.select { |name, number| number > 2 && name.includes?("r") }
puts planets

puts planets.select! { |name, number| number > 2 && name.includes?("r") }
puts planets
