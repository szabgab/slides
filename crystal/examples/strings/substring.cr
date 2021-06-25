text = "The black cat climbed the green tree"

puts text[0]
puts text[4]
puts text[0, 4]  # 4 characters (start, count)
puts text[0..4]  # 5 characters (Range)
# count cannot be negative, but the Range ending can and it means, from the end of the string
puts text[0..-4]


