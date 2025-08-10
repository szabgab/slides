if ARGV.size != 1
  puts "Need a filename on the command line"
  exit 1
end
filename = ARGV[0]

if File.exists?(filename)
  puts File.empty?(filename)
  puts File.size(filename)
else
  puts "File #{filename} does not exist"
end
