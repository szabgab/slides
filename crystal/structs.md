# Structs
{id: structs}

## Empty struct
{id: empty-struct}
{i: struct}

* [Struct API](https://crystal-lang.org/api/Struct.html)
* [Struct reference](https://crystal-lang.org/reference/syntax_and_semantics/structs.html)
* [use structs when possible](https://crystal-lang.org/reference/guides/performance.html#use-structs-when-possible)

![](examples/struct/empty_struct.cr)
![](examples/struct/empty_struct.out)

## Initialize immutable struct
{id: struct-initialize}
{i: initialize}

* There is no way to change this struct
* There is no way to access the individual attributes as there are no getters

![](examples/struct/initialize_struct.cr)
![](examples/struct/initialize_struct.out)

## Initialize immutable struct - shorthand
{id: struct-initialize-shorthand}

![](examples/struct/initialize_struct_shorthand.cr)
![](examples/struct/initialize_struct_shorthand.out)

## Immutable struct with getters
{id: struct-immutable-with-getters}

![](examples/struct/immutable_struct_with_getter.cr)
![](examples/struct/immutable_struct_with_getter.out)

## Immutable struct with getter macro
{id: struct-immutable-with-getter-macro}

![](examples/struct/immutable_struct_with_getter_macro.cr)
![](examples/struct/immutable_struct_with_getter_macro.out)

## Mutable Struct with propery macro
{id: struct-mutable-with-property-macro}

![](examples/struct/mutable_struct_with_property_macro.cr)
![](examples/struct/mutable_struct_with_property_macro.out)

## Struct with optional attributes
{id: struct-optional}

![](examples/struct/struct_optional.cr)

## Struct with initializer
{id: struct-with-initialized}

![](examples/struct/struct_with_initializer.cr)

## Struct with default value
{id: struct-with-deefault}

![](examples/struct/with_default_value.cr)

## Struct pass-by-value
{id: struct-pass-by-value}

![](examples/struct/struct_pass_by_value.cr)
![](examples/struct/struct_pass_by_value.out)

## Struct from JSON
{id: struct-from-json}
{i: JSON::Serializable}

* [JSON::Serializable](https://crystal-lang.org/api/JSON/Serializable.html)

![](examples/struct/struct_from_json.cr)
![](examples/struct/struct_from_json.out)

## Struct both from JSON and initialize
{id: struct-from-json-and-initialize}

![](examples/struct/struct_initialize_and_from_json.cr)
![](examples/struct/struct_initialize_and_from_json.out)

## Struct from JSON - manual parsing
{id: struct-from-json-manual-parsing}
{i: include}
{i: JSON::PullParser}

* [JSON::PullParser](https://crystal-lang.org/api/JSON/PullParser.html)

![](examples/struct/struct_from_json_pull_parser.cr)
![](examples/struct/struct_from_json_pull_parser.out)

## Multi-level struct from JSON
{id: struct-multi-level}

![](examples/struct/multi_level.cr)
![](examples/struct/multi_level.out)

## Extend struct
{id: struct-extend-struct}

![](examples/struct/extend_struct.cr)
![](examples/struct/extend_struct.out)

## Extend other structs
{id: struct-extend-other-structs}

![](examples/struct/integers.cr)


