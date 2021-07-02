planets = {
  "Mars"    => 1,
  "Jupyter" => 2,
  "Saturn"  => 3,
  "Earth"   => 4,
}
puts planets.reject("Mars")
puts planets

puts planets.reject!("Mars")
puts planets
