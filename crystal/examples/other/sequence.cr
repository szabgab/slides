def seq
  val = 0
  loop do
    val += 1
    yield val
  end
end

seq { |num|
  puts num
  break if num > 10
}
puts "after"
