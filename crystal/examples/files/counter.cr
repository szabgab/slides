# if file exists read the content


filename = "counter.txt"


counter = 0
if fh = File.exists?(filename)
    content = File.read(filename)
    counter = content.to_i
end

counter += 1
puts counter

File.write(filename, counter)
