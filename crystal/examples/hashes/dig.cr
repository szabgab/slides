planets = {
  "Mars" => {
    "Traveler" => "Elon",
    "People"   => "Green",
  },
  "Jupyter" => 2,
  "Saturn"  => 3,
  "Earth"   => 4,
}
# puts planets["Mars"]["People"]
# Error: undefined method '[]' for Int32 (compile-time type is (Hash(String, String) | Int32))

puts planets.dig "Mars", "People" # Green

# puts planets.dig "Mars", "Date"
# Unhandled exception: Missing hash key: "Date" (KeyError)

date = puts planets.dig? "Mars", "Date" # nil
puts date.nil?                          # true
