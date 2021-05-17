if ARGV.size != 1
    puts "Needs path to directory"
    exit 1
end

path = ARGV[0]

dr = Dir.new(path)
dr.children.each {|thing|
   puts thing
}
