(1..10).each { |ix|
  next if ix % 2 == 0
  break if ix == 7
  puts ix
}
