planets = ["Mars", "Jupyter", "Saturn", "Earth"]

planets.each { |planet| puts planet }

# enumerate
planets.each_with_index { |planet, idx|
  puts "#{idx}: #{planet}"
}
