# Numbers
{id: numbers}


## Numerical operations (integers)
{id: numerical-operations-integers}

* The division keeps the type so dividing one integer by another integer will always return an integer.

![](examples/numbers/calc.rs)
![](examples/numbers/calc.out)

## Increment integers
{id: increment-integers}

![](examples/numbers/increment.rs)
![](examples/numbers/increment.out)

## unfit in i8 - compile time
{id: unfit-in-i8-compile-time}

![](examples/numbers/small_integers_unfit_in_i8.rs)
![](examples/numbers/small_integers_unfit_in_i8.out)

## unfit in i8 - run time
{id: unfit-in-i8-run-time}

![](examples/numbers/increment_small_integers.rs)
![](examples/numbers/increment_small_integers.out)

## rounding float
{id: rounding-float}

![](examples/numbers/rounding_float.rs)
![](examples/numbers/rounding_float.out)

## Floating point imprecision
{id: floating-point-imprecision}

![](examples/numbers/floating_point_imprecision.rs)
![](examples/numbers/floating_point_imprecision.out)

## Compare integers
{id: compare-integers}
{i: cmp}
{i: Less}
{i: Greater}
{i: Equal}
{i: Ordering}

* We can use the regular `<`, `>`, `==` operators to compare any type of integers assuming the two sides are from the same type.
* The `cmp` method returns a value from the [Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html) enum.

![](examples/numbers/compare-integers/src/main.rs)

![](examples/numbers/compare-integers/out.out)


## Compare floating point numbers
{id: compare-floating-pount-numbers}

![](examples/numbers/compare-floats/src/main.rs)

![](examples/numbers/compare-floats/out.out)

## Compare floating point numbers by rounding
{id: compare-floating-point-numbers-by-rounding}
{i: round}

![](examples/numbers/compare-floats-by-rounding/src/main.rs)
![](examples/numbers/compare-floats-by-rounding/out.out)

## Approximately compare floating point numbers
{id: approximately-compare-floating-point-numbers}
{i: TBD}
{i: approx_eq}

* [ordered-float](https://crates.io/crates/ordered-float)
* [float-cmp](https://crates.io/crates/float-cmp)

![](examples/numbers/compare-floats-approximately/src/main.rs)
![](examples/numbers/compare-floats-approximately/out.out)


