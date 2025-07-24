h = Hash.new
puts h
h["fname"] = "Foo"
h["lname"] = "Bar"
puts h

h.keys.each do|key|
  puts "#{key} - #{h[key]}"
end
