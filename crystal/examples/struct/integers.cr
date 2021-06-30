struct Int
  def prime?
    (2..(self ** 0.5).to_i).each { |num|
      return false if self % num == 0
    }
    return true
  end
end

puts 23.odd?
puts 23.even?
puts 23.prime?
puts 20.prime?
