values = [0, "0", "", true, false, 1]
values.each {|val|
    if val
        puts "#{val} is true"
    else
        puts "#{val} is NOT true"
    end
}