result = `ls -l`
if $?.success?
  puts result
else
  puts "Failure"
end
