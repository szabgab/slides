macro t(name)
  print "%s %s\n" % {typeof({{name}}), {{name}}}
end

h = {a: 1, "a b-23": 2}
t h
h.each { |x, y|
  t x
  t y
}
