if ARGV.size != 1
    puts "Need a filename on the command line"
    exit 1
end
filename = ARGV[0]

content = File.read(filename)

puts content