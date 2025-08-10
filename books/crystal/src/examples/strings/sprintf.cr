name = "Foo"
number = 42

text = "The name is %s" % name
puts text

text = "The name is %s the number is %s" % {name, number} # Tuple
puts text

text = "The name is %s the number is %s" % [name, number] # Array
puts text

text = "The name is %{txt} the number is %{num}" % {txt: name, num: number} # NamedTuple
puts text

text = sprintf "The name is %s the number is %s", name, number
puts text
