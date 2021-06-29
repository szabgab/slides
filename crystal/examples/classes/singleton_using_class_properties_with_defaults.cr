class Options
  class_property repetition = 0
  class_property url = ""
  class_property verbose = false
end

puts Options.repetition
Options.repetition = 3
puts Options.repetition
puts Options.repetition + 1
