# Functions
{id: functions}

## Functions and methods
{id: functions-and-methods}

* [Overloading](https://crystal-lang.org/reference/syntax_and_semantics/overloading.html)
* [Type Restrictions](https://crystal-lang.org/reference/syntax_and_semantics/type_restrictions.html)
* [Method arguments](https://crystal-lang.org/reference/syntax_and_semantics/default_values_named_arguments_splats_tuples_and_overloading.html)
* [Return types](https://crystal-lang.org/reference/syntax_and_semantics/return_types.html)

## Function return value
{id: return-value}
{i: return}

![](examples/functions/return_value.cr)
![](examples/functions/return_value.out)


## Function parameter passing
{id: function-parameter-passing}

![](examples/functions/parameter_passing.cr)
![](examples/functions/parameter_passing.out)


## Function parameter default value
{id: function-parameter-default-value}
{i: default}

![](examples/functions/default_value.cr)
![](examples/functions/default_value.out)

* Type definition for parameters


![](examples/functions/parameter_types.cr)

## Wrong number of arguments
{id: wrong-number-of-arguments}

* We have a function that expect two integers. Can we instead pass an array of two integers?
* Normally no, but there are at least 3 solutions

![](examples/functions/pass_array_instead_of_individual_values.cr)

## Manually separate
{id: manually-separate}

![](examples/functions/manually_separate.cr)

## Tuple from
{id: tuple-from}

![](examples/functions/tuple_from.cr)


## Array overload
{id: array-overload}

![](examples/functions/array_overload.cr)

## Multiple dispatch
{id: multiple-dispatch}

* Multi-dispatch functions with same name but different signature

![](examples/functions/overloading.cr)

* Integers are also accepted when we are expecting floats

![](examples/functions/overloading_float_int.cr)


## Implicit return value
{id: implicit-return-value}

If there is no explocit `return` statement then the result of the last statement executed in the function will be
returned from the function.

![](examples/functions/implicit.cr)
![](examples/functions/implicit_return.cr)
![](examples/functions/implicit_return.out)

## Return Type definition
{id: return-type}

* The compile-time error only happens if we actually call the incorrect function.

![](examples/functions/return_type.cr)


## Type or Nil
{id: type-or-nil}
{i: ?}
{i: Nil}

* A question mark `?` after the type in the function declaration is the same as accepting `nil` as well.
* `Int32?` is the same as `Int32 | ::Nil`

![](examples/functions/type_or_nil.cr)

## Yield
{id: yield}

* [Blocks and Procs](https://crystal-lang.org/reference/syntax_and_semantics/blocks_and_procs.html)

![](examples/functions/yield.cr)

* Optionally you can add a `&anything` if you think that makes the code more readable, but the important part is having `yield` in the code.

![](examples/functions/yield_block.cr)


* You can call `yield` more than once inside the function and the block will be executed for every `yield`.

![](examples/functions/twice.cr)

## Yield with parameters
{id: yield-with-parameters}

![](examples/functions/yield_params.cr)

* This example based on the example on the Crystal web site does not work:

![](examples/functions/yield_both.cr)

## Block and parameters
{id: block-and-parameters}

![](examples/functions/yield_parameters.cr)


