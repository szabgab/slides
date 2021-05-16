planets = ["Mars", "Jupyter", "Saturn", "Earth"]
p! planets           # ["Mars", "Jupyter", "Saturn", "Earth"]
puts typeof(planets) # Array(String)
puts planets.size    # 4

mixed = [1, 3.14, "PI"]
puts typeof(mixed)   # Array(Float64 | Int32 | String)

