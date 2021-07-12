LIMIT = 20

hidden = Random.rand(LIMIT) + 1
puts "For debugging: #{hidden}"
loop do
  print "Guess a number between 1 and #{LIMIT}: "
  guess_str = gets.not_nil!
  if guess_str == "x"
    puts "Good bye"
    break
  end

  guess = guess_str.to_i

  if guess == hidden
    puts "Matched!"
    break
  elsif guess < hidden
    puts "Too small"
  else
    puts "Too big"
  end
end
