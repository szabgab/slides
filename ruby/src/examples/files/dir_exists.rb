
if ARGV.length != 1
  puts "Usage: #{$0} DIRNAME"
  exit
end

dirname = ARGV[0]
if Dir.exists? dirname
  puts "#{dirname} exists"
else
  puts "#{dirname} does NOT exist"
end
