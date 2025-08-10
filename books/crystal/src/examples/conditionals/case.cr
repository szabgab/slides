if ARGV.size != 1
  puts "Usage: case.cr DIRECTION"
  exit -1
end
direction = ARGV[0]

case direction
when "forward"
  puts "go on"
when "bacward"
  puts "go back"
when "left", "right"
  puts "go #{direction}"
else
  puts "We don't know how to go '#{direction}'"
  exit 0
end
