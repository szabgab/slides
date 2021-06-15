def is_odd(n : Int32) : Bool
  return n % 2 == 1
end

def is_even(n : Int32) : Bool
  return n
end

x = is_odd(2)
y = is_even(2)

#  5 | def is_even(n : Int32) : Bool
# Error: method top-level is_even must return Bool but it is returning Int32
