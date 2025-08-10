puts "before"
ch = Channel(Int32).new

puts "before spawn"
spawn do
  puts "in spawn before send"
  ch.send 42
  puts "in spawn after send"
end

puts "before receive"
res = ch.receive
puts "received #{res}"
