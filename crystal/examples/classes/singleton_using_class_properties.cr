class Options
    class_property repetition : Int32|Nil
    class_property url = String
    class_property verbose = Bool
end

puts Options.repetition
Options.repetition = 3
puts Options.repetition
if ! Options.repetition.nil?
    puts Options.repetition + 1
end

