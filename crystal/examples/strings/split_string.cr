text = "This is a  string"
puts text
pieces = text.split(" ")
puts pieces # ["This", "is", "a", "", "string"]

pieces = text.split(/ +/)
puts pieces # ["This", "is", "a", "string"]

text = "name:secret"
name, password = text.split(":")
puts name
puts password
