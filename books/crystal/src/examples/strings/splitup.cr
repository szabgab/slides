text = "1234567890123"
width = 3
# (0..text.size).step(width) {|start|
#    puts text[start, width]
# }

res = ((0..text.size).step(width).map { |start| text[start, width] }).join " "
puts res
