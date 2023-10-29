# Rust types
{id: types}


## Rust Type system
{id: rust-type-system}

## Rust numerical operations
{id: rust-numerical-operations}

![](examples/types/numerical-operations/src/main.rs)

## Rust numerical types
{id: rust-numerical-types}
{i: i32}
{i: i64}

* By default numbers are stored in i32 whose range is -2147483648..=2147483647
* We can explicitely put numbers in different types

![](examples/types/number-types/src/main.rs)

![](examples/types/numbers/src/main.rs)

* List of Rusts [primitive types](https://doc.rust-lang.org/core/primitive/index.html)

## Rust type mismatch in numerical operation
{id: rust-type-mismatch-in-numerical-operation}

![](examples/types/type-mismatch/src/main.rs)

* TODO: if we remove the i32 then this works even though, I think, the default is i32


## Rust Overflow
{id: rust-overflow}

![](examples/types/overflow/src/main.rs)
![](examples/types/overflow/out.out)

