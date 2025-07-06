
if ARGV.length != 1
  puts "Usage: #{$0} FILENAME"
  exit
end

filename = ARGV[0]
File.write(filename, 'My second line\n', mode: 'a')
