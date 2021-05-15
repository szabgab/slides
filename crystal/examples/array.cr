planets = ["Mars", "Jupyter", "Saturn", "Earth"]
p! planets           # ["Mars", "Jupyter", "Saturn", "Earth"]
puts typeof(planets) # Array(String)
puts planets.size    # 4

mixed = [1, 3.14, "PI"]
puts typeof(mixed)   # Array(Float64 | Int32 | String)




empty = [] of Int32
empty << 23
# empty << 3.14  # Error: no overload matches 'Array(Int32)#<<' with type Float64

