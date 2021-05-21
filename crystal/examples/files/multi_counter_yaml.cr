require "yaml"

filename = "counter.yaml"

counters = {} of String => Int32
if File.exists?(filename)
    content = File.new(filename)
    counters = Hash(String, Int32).from_yaml(content)
end


if ARGV.size == 1
    name = ARGV[0]
    if ! counters.has_key?(name)
        counters[name] = 0
    end
    counters[name] += 1
    puts counters[name]
    File.write(filename, counters.to_yaml)
else
    counters.each {|arg, i|
        puts "#{i}: #{arg}"
    }
end




