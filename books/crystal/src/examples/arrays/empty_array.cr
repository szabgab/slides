# empty = []       # Syntax error

empty = [] of Int32
puts empty.size   # 0
puts empty.empty? # true

empty << 23
puts empty.size   # 1
puts empty.empty? # false

# empty << 3.14  # Error: no overload matches 'Array(Int32)#<<' with type Float64

other = Array(Int32).new
puts typeof(other) # Array(Int32)
puts other.size    # 0
