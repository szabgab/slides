if ARGV.size != 2
    puts "Needs two numbers: the two sides of the rectangle"
    exit 1
end

width, height = ARGV
puts width
puts height

area = width.to_f * height.to_f
circumference = 2 * (width.to_f + height.to_f)
puts "area: #{area}"
puts "circumference: #{circumference}"
