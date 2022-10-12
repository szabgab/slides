
if ARGV.length != 1
  puts "Usage: #{$0} DIRNAME"
  exit
end

dirname = ARGV[0]
d = Dir.mkdir dirname
puts d
