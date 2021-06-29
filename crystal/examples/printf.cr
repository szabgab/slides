# Padding and Alignment
number = 42
printf "'%-4s'\n", number # Padding, left align
printf "'%4s'\n", number  # Padding, right align
printf "'%04s'\n", number # Padding with 0s

# Rounding floating point
puts Math::PI
printf "'%d'\n", Math::PI
printf "'%f'\n", Math::PI
printf "'%.3f'\n", Math::PI
