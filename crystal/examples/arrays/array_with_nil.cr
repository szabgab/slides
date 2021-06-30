n = 5
nums = (0_i64.as(Int64 | Nil)..n).to_a
puts typeof(nums) # Array(Int64 | Nil)

other = [nil] + (1..n).to_a
puts typeof(other) # Array(Int32 | Nil)
