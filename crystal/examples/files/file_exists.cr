if ARGV.size != 1
    puts "Need a filename on the command line"
    exit 1
end
filename = ARGV[0]


if File.exists?(filename)
    puts "Exists"
else
    puts "Does NOT exist"
end
