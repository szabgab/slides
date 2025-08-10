def run(&block)
  puts "before"
  yield
  puts "after"
end

run {
  puts "in block"
}
