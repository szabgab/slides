class Object
    macro methods
        {{ @type.methods.map &.name.stringify }}
    end
end

puts Bool.methods
puts Int32.methods
puts Array.methods
puts Hash.methods
