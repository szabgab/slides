if ARGV.size != 1
  puts "Need a filename on the command line"
  exit 1
end
filename = ARGV[0]

File.each_line(filename) { |line|
  puts line
}
