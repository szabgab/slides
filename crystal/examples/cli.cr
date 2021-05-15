puts ARGV
puts ARGV.size

ARGV.each_with_index {|arg, i|
    puts "Argument #{i} was #{arg}"
}