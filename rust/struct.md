# struct
{id: struct}

## Create simple struct
{id: create-simple-struct}
{i: struct}

![](examples/struct/point/src/main.rs)
![](examples/struct/point/out.out)

## Change attributes of a mutable struct
{id: mutable-struct}

![](examples/struct/mutable-point/src/main.rs)
![](examples/struct/mutable-point/out.out)

## Struct method to modify fields
{id: struct-method-to-modify-fields}

![](examples/struct/point-with-method/src/main.rs)
![](examples/struct/point-with-method/out.out)

## Struct inheritance
{id: struct-inheritance}

* There is no inheritance among structs similar to classes in other languages. However, there is composition.

## Struct composition
{id: struct-composition}

![](examples/struct/circle-compose/src/main.rs)
![](examples/struct/circle-compose/out.out)

## Struct duplicate
{id: struct-duplicate}

![](examples/struct/circle-duplicate/src/main.rs)
![](examples/struct/circle-duplicate/out.out)

## Printing struct fails
{id: printing-struct-fails}

![](examples/struct/printing-struct-fails/src/main.rs)

## Print struct (Point)
{id: print-struct}
{i: std::fmt::Display}
{i: Display}

![](examples/struct/print-point/src/main.rs)
![](examples/struct/print-point/out.out)

## Debug struct (Point)
{id: debug-struct}
{i: std::fmt::Debug}
{i: Debug}

![](examples/struct/debug-point/src/main.rs)
![](examples/struct/debug-point/out.out)

## Print complex struct
{id: print-complex-struct}

![](examples/struct/printing-struct/src/main.rs)
![](examples/struct/printing-struct/out.out)

## Debug complex struct
{id: debug-complex-struct}

![](examples/struct/debugging-struct/src/main.rs)
![](examples/struct/debugging-struct/out.out)

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

## Compare structs for partial equality
{id: compare-structs-for-partial-equality}
{i: struct}
{i: PartialEq}

![](examples/struct/compare_structs_for_equality.rs)

