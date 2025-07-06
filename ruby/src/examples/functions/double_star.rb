def report(**kw)
  puts kw.class # Hash
  puts kw
end

report()
report("math" => 99, "biology" => 88)
