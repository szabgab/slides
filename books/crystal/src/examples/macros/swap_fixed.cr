macro swap(a, b)
  %temp = {{a}}
  {{a}} = {{b}}
  {{b}} = %temp
end

temp = "z"
x = "x"
y = "y"
swap(x, y)
p! x
p! y
p! temp
