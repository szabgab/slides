planets = ["Mars", "Jupyter", "Saturn", "Earth"]
p! planets                # ["Mars", "Jupyter", "Saturn", "Earth"]
puts typeof(planets)      # Array(String)
puts planets.size         # 4

integers = [3, 8, -2]
puts typeof(integers)     # Array(Int32)

floats = [3.14, 2.1]
puts typeof(floats)       # Array(Float64)

mixed = [1, 3.14, "PI"]
puts typeof(mixed)        # Array(Float64 | Int32 | String)

