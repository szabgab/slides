text = "123456789112777"
count = [0] * 10

text.each_char {|chr| 
    count[chr.to_i] += 1
}

count.each_with_index {|value, idx|
    puts "#{idx} #{value}"
}