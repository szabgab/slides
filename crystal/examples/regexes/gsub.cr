puts "The cat is here".gsub("cat", "dog")
puts "The cat is here".gsub("cat") { "dog" }

# puts "The cat is here".gsub("cat") { |match| match.reverse }
# ameba: Use short block notation instead
puts "The cat is here".gsub("cat", &.reverse)

# puts "The cat is here".gsub(/c../) { |match| match.reverse }
# ameba: Use short block notation instead
puts "The cat is here".gsub(/c../, &.reverse)
