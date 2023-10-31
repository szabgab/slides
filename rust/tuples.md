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

## Create tuple with types, but without values
{id: create-tuple-with-types-but-without-values}

* We can create a tuple without initializing. In this case it seems even more usefule to declare the types. (Though not required.)
* Then later we can assign all the values at once.
* We cannot assign them one-by-one.

![](examples/tuples/create-tuple-without-values/src/main.rs)
![](examples/tuples/create-tuple-without-values/out.out)


## Destructuring tuple
{id: destructuring-tuple}
{i: _}

* It is not *destructing*! Just looks similar.
* It means to taking the values of a tuple apart into individual variables.
* We havae to assign all the value

![](examples/tuples/destructuring-tuple/src/main.rs)
![](examples/tuples/destructuring-tuple/out.out)

## The empty tuple is called the unit
{id: empty-tuple-unit}
{i: unit}
{i: ()}

* An empty pair of parentheses `()` creates an empty tuple, also called a [unit](https://doc.rust-lang.org/std/primitive.unit.html).
* Functions that don't return anything return the same `unit` value.

![](examples/tuples/empty/src/main.rs)
![](examples/tuples/empty/out.out)

## One element tuple
{id: one-element-tuple}

* We can create a one-element tuple by putting a comma after the element, but probably there is not much value in it.
* Probably it is better to just create a variable holding that single value.

![](examples/tuples/one-element/src/main.rs)
![](examples/tuples/one-element/out.out)

