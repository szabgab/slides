
if ARGV.length != 1
  puts "Usage: #{$0} DIRNAME"
  exit
end

dirname = ARGV[0]

content = Dir.glob(dirname)
print content

