class Point
  property x : Float64
  property y : Float64

  def initialize(@x, @y)
  end

  def to_s
    return "(#{@x}, #{@y})"
  end
end

p = Point.new(2.1, 3.4)
puts p
puts p.to_s
