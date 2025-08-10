require "http/client"
puts "before"
ch = Channel(HTTP::Client::Response).new

puts "before spawn"
spawn do
  puts "in spawn before send"
  res = HTTP::Client.get "https://code-maven.com/"
  ch.send res
  puts "in spawn after send"
end

puts "before receive"
res = ch.receive
puts "received #{res.body.size} bytes including this row: #{res.body.lines.select(/<title>/)}"
