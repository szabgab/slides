macro define_method(name, content)
  puts "before"
  def {{name}}
    puts {{content}}
  end
  puts "after"
end

define_method foo, 1

puts "before foo"
foo # => 1
puts "after foo"


