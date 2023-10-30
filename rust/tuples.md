# Tuples in Rust
{id: tuple}

## Rust tuple - fixed-sizes, mixed, ordered collection
{id: rust-tuple}
{i: tuple}

* Each value can be any type. (heterogeneous)
* The types and the number of elements are fixed at creation.
* In this example the types are deducted from the values.
* It is ordered.

* The content can be changed only if the definition uses `mut`.
* [Tuple](https://doc.rust-lang.org/std/primitive.tuple.html)
* [Tuple Types](https://doc.rust-lang.org/reference/types/tuple.html)
* [Examples](https://doc.rust-lang.org/rust-by-example/primitives/tuples.html)

![](examples/tuples/create-tuple/src/main.rs)
![](examples/tuples/create-tuple/out.out)

## Define the types in the tuple
{id: define-the-types-in-the-tuple}

* Optionally we an define the types of elements of a tuple.
* This can be useful if we don't want the default types. (e.g the default integer type is `i32`, but here we use `i8`.)

![](examples/tuples/define-types/src/main.rs)
![](examples/tuples/define-types/out.out)

## Change tuple (mutable)
{id: change-tuple}
{i: mut}

![](examples/tuples/change-tuple/src/main.rs)
![](examples/tuples/change-tuple/out.out)

## Destructuring tuple
{id: destructuring-tuple}

![](examples/tuples/destructuring-tuple/src/main.rs)

## Tuple
{id: tuple-example}

![](examples/tuples/tuple/src/main.rs)

## The empty tuple is called the unit
{id: empty-tuple-unit}

* An empty pair of parentheses `()` creates an empty tuple, also called a `unit`.
* Functions that don't return anything return the same `unit` value.

![](examples/tuples/empty/src/main.rs)

## One element tuple
{id: one-element-tuple}

* This works, but do we need it?

![](examples/tuples/one-element/src/main.rs)

