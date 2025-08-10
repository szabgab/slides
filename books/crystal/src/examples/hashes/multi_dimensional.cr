planets = {
  "Mars" => {
    "color" => "Red, brown and tan.",
  },
  "Jupyter" => {
    "color" => "Brown, orange and tan, with white cloud stripes.",
  },
  "Saturn" => {
    "color" => "Golden, brown, and blue-grey.",
  },
  "Earth" => {
    "color" => "Blue, brown green and white.",
  },
}

puts planets["Mars"]["color"]

# puts planets["Mercury"]
# Unhandled exception: Missing hash key: "Mercury" (KeyError)

# puts planets["Mars"]["rover"]
# Unhandled exception: Missing hash key: "rover" (KeyError)
