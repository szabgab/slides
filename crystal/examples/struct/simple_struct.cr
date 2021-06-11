struct MyConfig
  property name : String?
  property address : String?
end

cfg = MyConfig.new
puts cfg

cfg.name = "Foo"
puts cfg

cfg.address = "foo@bar.com"
puts cfg

