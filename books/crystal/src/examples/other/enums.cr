enum Direction : UInt8
  Left
  Right
  Up
  Down

  def left?
    self == Direction::Left
  end
end

puts Direction::Left
puts Direction::Left.value
puts Direction::Right
dir = Direction::Left
puts dir.left?

dir = Direction::Right
puts dir.left?
