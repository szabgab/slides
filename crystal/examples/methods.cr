class Object
    macro methods
        {{ @type.methods.map &.name.stringify }}
    end
end

p! Bool.methods
p! String.methods
p! Int32.methods
p! Array.methods
p! Hash.methods
