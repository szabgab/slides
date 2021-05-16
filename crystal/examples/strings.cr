text = "The black cat climbed the green tree"
puts text.size
puts text.empty?
puts text.blank?
puts text.reverse

puts text.includes?("cat")
puts text.includes?("dog")
puts text.starts_with?("The")
puts text.starts_with?("the")
puts text.ends_with?("tree")
puts text.index("cat")
puts text.index("dog")

puts text.index("c")
puts text.rindex("c")

puts text[0]
puts text[4]
puts text[0, 4]  # 4 characters (start, count)
puts text[0..4]  # 5 characters (Range)
# count cannot be negative, but the Range ending can and it means, from the end of the string
puts text[0..-4]

new_text = text.sub("cat", "dog")
puts text
puts new_text
new_text = text.sub("dog", "elephant")