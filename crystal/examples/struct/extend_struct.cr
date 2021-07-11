struct MyConfig
end

cfg = MyConfig.new
p! cfg
p! typeof(cfg)

struct MyConfig
  property name : String?
end

cfg.name = "Foo"
p! cfg
