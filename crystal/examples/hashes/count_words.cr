words = ["cat", "dog", "snake", "cat", "bug", "ant", "cat", "dog"]
count = {} of String => Int32

words.each { |word|
  if !count.has_key?(word)
    count[word] = 0
  end
  count[word] += 1
}

count.each { |word, cnt|
  puts "#{word} #{cnt}"
}
