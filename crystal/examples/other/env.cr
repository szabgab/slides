ENV.keys.sort.each { |key|
  puts "%-25s %s" % {key, ENV[key]}
}
