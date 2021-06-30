text = "ab  text. and $ and ^ also"
puts text
puts text.sub(/\W/, "")
puts text.gsub(/\W/, "")
