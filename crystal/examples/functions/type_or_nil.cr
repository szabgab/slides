def func(number : Int32?)
  puts number
end

func(23)
func(nil)

# func()
# Error: wrong number of arguments for 'func' (given 0, expected 1)

# func(2.3)
# Error: no overload matches 'func' with type Float64

def show(number : Int32)
  puts number
end

show(23)
# show(nil)
# Error: no overload matches 'show' with type Nil

def other(number : Int32 | ::Nil)
  puts number
end

other(23)
other(nil)

