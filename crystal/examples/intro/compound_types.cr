x = ["Foo", 42]
p! typeof(x)      # typeof(x) # => Array(Int32 | String)

a = {"Foo", 42}
p! typeof(a)      # typeof(a) # => Tuple(String, Int32)

y = {
  "name" => "Foo Bar",
  "id" => 42
}
p! typeof(y)      # typeof(y) # => Hash(String, Int32 | String)

z = {
  "name": "Foo Bar",
  "id": 42
}
p! typeof(z)      # typeof(z) # => NamedTuple(name: String, id: Int32)
