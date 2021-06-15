def foo
  puts "foo before"
  yield
  puts "foo after"
end

def bar
  puts "bar before"
  yield
  puts "bar after"
end


foo bar {
  puts "in block"
}

puts "----"

foo bar do
  puts "in do-end"
end
