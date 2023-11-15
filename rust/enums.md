# Enum
{id: enum}

## Enumeration
{id: enumeration}
{i: enum}
{i: PartialEq}
{i: dead_code}

* [Defining an enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)


![](examples/enums/weekdays/src/main.rs)

## Enumeration colors
{id: enumeration-colors}
{i: enum}
{i: dead_code}
{i: PartialEq}

* Create an enum with some values

![](examples/enums/colors-partial-equal/src/main.rs)
![](examples/enums/colors-partial-equal/out.out)


## Enumerate without PartialEq using match
{id: enumerat-with-match}
{i: enum}
{i: match}
{i: dead_code}

* If we don't have PartialEq on an enum and we don't want to add it or cannot add it (e.g. because it was supplied by an external crate) we can use `match`:

![](examples/enums/colors-match/src/main.rs)
![](examples/enums/colors-match/out.out)


## Struct using enum
{id: struct-using-enum}
{i: struct}
{i: enum}

![](examples/enums/colors-struct/src/main.rs)
![](examples/enums/colors-struct/out.out)

## Enums with embedded values and comparing them with match
{id: enums-with-embedded-values}
{i: enum}

![](examples/enums/colors-enum-with-value/src/main.rs)
![](examples/enums/colors-enum-with-value/out.out)


