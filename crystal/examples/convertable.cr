values = ["42", "42.1", "abc", "0"]
values.each {|val|
    puts val
    puts val.to_i?
    if val.to_i?
        puts "Convertable to Int32"
    end

    puts val.to_f?
    if val.to_f?
        puts "Convertable to Floar64"
    end
    puts "---"
}

