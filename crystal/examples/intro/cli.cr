puts ARGV
puts ARGV.size

ARGV.each_with_index { |arg, ix|
  puts "Argument #{ix} was #{arg}"
}

if ARGV.size > 0
  puts ARGV[0]
end
