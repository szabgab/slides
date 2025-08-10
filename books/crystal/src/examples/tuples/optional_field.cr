require "json"

alias Person = NamedTuple(
  name: String,
  email: String?,
)

p1_str = %[{"name": "Foo", "email": "foo@bar.com"}]
p1 = Person.from_json(p1_str)
p p1

p2_str = %[{"name": "Bar"}]
p2 = Person.from_json(p2_str)
# Unhandled exception: Missing json attribute: email
p p2

p3_str = %[{"name": "Bar", "email": null}]
p3 = Person.from_json(p3_str)
p p3

# {name: "Foo", email: "foo@bar.com"}
# {name: "Bar", email: nil}
# {name: "Bar", email: nil}
