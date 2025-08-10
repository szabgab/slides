if ARGV.size != 2
  puts "Need a filename and the content to write to it on the command line"
  exit 1
end
filename, content = ARGV

File.write(filename, content)
