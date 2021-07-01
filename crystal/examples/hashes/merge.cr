planets = {
  "Mars"    => 1,
  "Jupyter" => 2,
  "Saturn"  => 3,
  "Earth"   => 4,
}
puts planets
puts planets.merge({"Venus" => 5, "Mars" => 10})
puts planets

puts planets.merge!({"Pluto" => 5, "Mars" => 20})
puts planets
