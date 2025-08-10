def cond(x)
  if x > 5
    return x
  end
end

[3, 6].each { |value|
  puts value
  res = cond(value)
  puts res
  puts typeof(res)

  # puts res+1
  # Error: undefined method '+' for Nil (compile-time type is (Int32 | Nil))

  if !res.nil?
    puts res + 1
  end
}
