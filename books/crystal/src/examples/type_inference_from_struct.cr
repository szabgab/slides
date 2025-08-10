struct Dog
  getter name : String
  getter owner : String

  def initialize(@name, @owner)
  end
end

struct Cat
  getter name : String
  getter staff : String

  def initialize(@name, @staff)
  end
end

if Random.rand < 0.5
  animal = Dog.new("Gin", "Foo")
else
  animal = Cat.new("Tonic", "Bar")
end

p! animal
p! animal.class

# if animal.class == Cat
#  p! animal.staff
# else
#  p! animal.owner
# end

if animal.is_a?(Cat)
  p! animal.staff
else
  p! animal.owner
end

case animal
when Cat
  puts "cat"
  p! animal.staff
when Dog
  puts "dog"
  p! animal.owner
else
  puts "other"
end
