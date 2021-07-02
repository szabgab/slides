square = ->(x : Int32) { x * x }
puts typeof(square) # Proc(Int32, Int32)
puts square.call(3) # 9
