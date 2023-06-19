# Tuples in Rust
{id: tuple}

## Rust tuple - fixed-sizes, mixed, ordered collection
{id: rust-tuple}
{i: tuple}

* Each value can be any type. (heterogeneous)
* The types and the number of elements are fixed at creation.
* It is ordered.

* The content can be chnaged if the definition uses `mut`.
* [Tuple](https://doc.rust-lang.org/std/primitive.tuple.html)

![](examples/tuples/create_tuple.rs)

## Define the types in the tuple
{id: define-the-types-in-the-tuple}

* Can be useful if we don't want the default types.

![](examples/tuples/define_types.rs)

## Destructuring tuple
{id: destructuring-tuple}

![](examples/tuples/destructuring_tuple.rs)

## Tuple
{id: tuple-example}

![](examples/tuples/tuple.rs)

## Change tuple (mutable)
{id: change-tuple}

![](examples/tuples/change_tuple.rs)

## The empty tuple is called the unit
{id: empty-tuple-unit}

* An empty pair of parentheses `()` creates an empty tuple, also called a `unit`.
* Functions that don't return anything return the same `unit` value.

![](examples/tuples/empty.rs)

## One element tuple
{id: one-element-tuple}

* This works, but do we need it?

![](examples/tuples/one.rs)

