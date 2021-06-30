planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
puts planets.delete("Earth")
puts planets

res = planets.delete("Pluto")
puts res.nil?
puts planets

names = ["Foo", "Bar", "Foo"]
names.delete("Foo")
puts names
