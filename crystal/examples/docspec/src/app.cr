
# ```
# >> anagram?("abc", "bca") # => true
# >> anagram?("abc", "abd") # => false
# ```
def anagram?(x, y)
  return x.split("").sort() == y.split("").sort()
end
