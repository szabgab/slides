planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
puts planets[0]  # Mercury
puts planets[1]  # Venus
puts planets[-1] # Jupiter

puts planets[0, 3]  # ["Mercury", "Venus", "Earth"]
puts planets[0..3]  # ["Mercury", "Venus", "Earth", "Mars"]
puts planets[0...3] # ["Mercury", "Venus", "Earth"]

