# Convert string to number
{id: string-to-number}

## Convert string to (integer) number

{id: rust-convert-string-to-number}
{i: i32}
{i: parse}
{i: expect}

* In the printing we won't see the difference, but we can do numberical operations on numbers

![](examples/convert/string_to_int.rs)
![](examples/convert/string_to_int.out)

## Convert string to number that ends with newline
{id: rust-convert-string-to-number-end-with-newline}
{i: trim}

![](examples/convert/string_to_int_fail.rs)
![](examples/convert/string_to_int_fail.out)

## Convert string to number after removing whitespaces
{id: rust-convert-string-to-number-trim}
{i: trim}

![](examples/convert/string_to_int_trim.rs)
![](examples/convert/string_to_int_trim.out)

## Convert string to float
{id: convert-string-to-float}
{i: f32}

* Sometimes we are expecting floating point numbers.

![](examples/convert/string_to_float.rs)
![](examples/convert/string_to_float.out)


