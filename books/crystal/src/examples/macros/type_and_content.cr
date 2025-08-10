macro t(name)
  print "%s %s\n" % {typeof({{name}}), {{name}}}
end

h = {"a" => 1, "b-1" => 2}
t h
