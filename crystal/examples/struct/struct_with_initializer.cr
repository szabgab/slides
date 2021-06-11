struct MyConfig
  property name : String?
  property address : String?
  def initialize(@name)
  end
end

# empty_cfg = MyConfig.new()
# Error: wrong number of arguments for 'MyConfig.new' (given 0, expected 1)

cfg = MyConfig.new(name: "Foo")
puts cfg

cfg.address = "foo@bar.com"
puts cfg

