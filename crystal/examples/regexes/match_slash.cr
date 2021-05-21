text = "some/path"
match = /\/(.*)/.match(text)
if match
    puts match.[1]
end


match = %r{/(.*)}.match(text)
if match
    puts match.[1]
end
