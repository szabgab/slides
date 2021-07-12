LIMIT = 20

hidden = Random.rand(LIMIT) + 1
puts "For debugging: #{hidden}"
print "Guess a number between 1 and #{LIMIT}: "
guess = gets.not_nil!.to_i

if guess == hidden
  puts "Matched!"
elsif guess < hidden
  puts "Too small"
else
  puts "Too big"
end
