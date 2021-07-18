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

if prs["title"].nil?
  puts "nil"
else
  puts "not nil"
  puts prs["title"].size
end
