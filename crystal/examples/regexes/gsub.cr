puts "The cat is here".gsub("cat", "dog")
puts "The cat is here".gsub("cat") { "dog" }

puts "The cat is here".gsub("cat") { |match| match.reverse }
puts "The cat is here".gsub(/c../) { |match| match.reverse }
