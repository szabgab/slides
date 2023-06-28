# Loops in Rust
{id: loops}

## Three types of loops in Rust
{id: three-types-of-loops}

* `while`
* `loop`
* `for`

Two loop controls

* `break`
* `continue`

## While loop in Rust
{id: rust-while-loop}
{i: while}

* We usually use a `while` loop if we don't know how many iterations we'll have to do.

![](examples/loops/while.rs)

## Rust: loop with break
{id: rust-loop-with-break}
{i: loop}
{i: break}

* If we cannot have the condition at the top in some languages we write `while true`. In Rust we use `loop`.
* We better have a condition with a `break` or we create an infinite loop!

![](examples/loops/loop.rs)

## for loop in Rust
{id: rust-for-loop}
{i: for}
{i: range}

* If we want to iterate over a set of elements, eg. a range of numbers, then we ususally use `for`.
* `1..5` means the right-hand limit is NOT included.
* `1..=5` means the right-hand limit is included

![](examples/loops/for_loop.rs)
![](examples/loops/for_loop.out)


