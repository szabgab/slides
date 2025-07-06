def with_splat(*things)
  puts things.class
end

with_splat()
with_splat("Name", 23)

