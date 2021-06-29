require "json"

alias Thing = NamedTuple(name: String, number: Int32)

thing_json = %{{"name": "table", "number": 3}}
puts thing_json

tg = Thing.from_json(thing_json)
puts tg
