# struct
{id: struct}

## Create simple struct
{id: create-simple-struct}
{i: struct}

![](examples/struct/point.rs)
![](examples/struct/point.out)

## Change attributes of a mutable struct
{id: mutable-struct}

![](examples/struct/mutable_point.rs)
![](examples/struct/mutable_point.out)

## Struct method to modify fields
{id: struct-method-to-modify-fields}

![](examples/struct/point_with_method.rs)
![](examples/struct/point_with_method.out)

## Struct inheritance
{id: struct-inheritance}

* There is no inheritance among structs similar to classes in other languages. However, there is composition.

## Struct composition
{id: struct-composition}

![](examples/struct/circle_compose.rs)
![](examples/struct/circle_compose.out)

## Struct duplicate
{id: struct-duplicate}

![](examples/struct/circle_duplicate.rs)
![](examples/struct/circle_duplicate.out)

## Printing struct fails
{id: printing-struct-fails}

![](examples/struct/printing_struct_fails.rs)

## Print struct (Point)
{id: print-struct}
{i: std::fmt::Display}
{i: Display}

![](examples/struct/print_point.rs)
![](examples/struct/print_point.out)

## Debug struct (Point)
{id: debug-struct}
{i: std::fmt::Debug}
{i: Debug}


![](examples/struct/debug_point.rs)
![](examples/struct/debug_point.out)

## Print complex struct
{id: print-complex-struct}

![](examples/struct/printing_struct.rs)
![](examples/struct/printing_struct.out)

## Debug complex struct
{id: debug-complex-struct}

![](examples/struct/debugging_struct.rs)
![](examples/struct/debugging_struct.out)

## Struct with vector and optional value
{id: struct-with-vector-and-optional-value}

![](examples/struct/struct_with_vector_and_optional_value.rs)
![](examples/struct/struct_with_vector_and_optional_value.out)

## Printing and debug-printing simple struct
{id: printing-simple-struct}

![](examples/struct/struct_cannot_be_printed.rs)
![](examples/struct/struct_with_debug.rs)
![](examples/struct/struct_with_debug.out)
![](examples/struct/struct_with_display.rs)
![](examples/struct/struct_with_display.out)

## Use a tuple as a struct to represent color
{id: use-a-typle-as-struct}

![](examples/struct/tuple_as_struct.rs)
![](examples/struct/tuple_as_struct.out)

## Add method to tuple-based struct
{id: method-to-tuple-based-struct}

![](examples/struct/tuple_as_struct_method.rs)
![](examples/struct/tuple_as_struct_method.out)

## Struct with method
{id: struct-with-method}

![](examples/struct/struct_with_method.rs)
![](examples/struct/struct_with_method.out)

## Structs and circural references
{id: structs-and-circular-references}

![](examples/struct/circural_references.rs)

## Multiple referene to a struct
{id: multiple-reference-to-a-struct}

![](examples/struct/multiple_referene_to_struct.rs)

## new method with default values for struct
{id: new-method-with-default-values}
{i: new}

![](examples/struct/new.rs)

## The new method has no special feature
{id: new-method-no-special-feature}
{i: new}

* We could use any other name instead of `new`. For example we could use `qqrq` as well.
* The name `new` is only to give the power of familiarity.

![](examples/struct/qqrq.rs)


## Default values
{id: default-values}

![](examples/struct/default.rs)

## Default for composite struct
{id: default-for-composite-struct}

![](examples/struct/default_for_composite_struct.rs)

