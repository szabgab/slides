if Random.rand < 0.5
  prs = {
    "name"  => "Foo",
    "title" => "Manager",
  }
else
  prs = {
    "name"  => "Foo",
    "title" => nil,
  }
end

p! prs

title = prs["title"]
if title.nil?
  puts "nil"
else
  puts "not nil"
  puts title.size
end

if title = prs["title"]
  puts "not nil"
  puts title.size
else
  puts "nil"
end
