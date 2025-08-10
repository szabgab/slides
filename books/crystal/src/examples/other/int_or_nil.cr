text = "Black cat"
idx = text.index("cat")
puts typeof(idx) # (Int32 | Nil)

# puts text[idx]
# Error: no overload matches 'String#[]' with type (Int32 | Nil)

if idx.is_a?(Int32)
  puts typeof(idx) # Int32
  puts text[idx]
end
