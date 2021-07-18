if Random.rand < 0.5
  x = "abc"
else
  x = nil
end

if x.nil?
  puts "nil"
else
  puts x
  puts x.size
end
