struct MyConfig
end

cfg = MyConfig.new
puts cfg
puts typeof(cfg)

struct MyConfig
  property name : String?
end

cfg.name = "Foo"
puts cfg
#
# cfg.address = "foo@bar.com"
# puts cfg
