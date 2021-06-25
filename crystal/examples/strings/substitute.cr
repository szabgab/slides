text = "The black cat climbed the green tree"

new_text = text.sub("cat", "dog")
puts text
puts new_text

new_text = text.sub("dog", "elephant")
puts text
puts new_text

text = "Red cat, Blue cat"
new_text = text.sub("cat", "dog")
puts text
puts new_text

animal = "cat"
new_text = text.sub animal, do |original|
   original.upcase
end
puts new_text
