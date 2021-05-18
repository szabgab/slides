values = [0, "0", "", 1, true, false, nil]
values.each {|val|
    if val
        puts "#{val} is true"
    else
        puts "#{val} is NOT true"
    end
}