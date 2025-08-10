module Tools
  def screwdriver
    puts "Screwdriver"
  end
end

class Device
  include Tools
end

x = Device.new
p! x
x.screwdriver
