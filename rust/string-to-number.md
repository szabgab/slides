# Convert string to number
{id: string-to-number}

## Convert string to (integer) number - parse, turbofish

{id: rust-convert-string-to-number}
{i: i32}
{i: parse}
{i: expect}
{i: ::<>()}

* In the printing we won't see the difference, but we can do numberical operations on numbers.
* We can either define the expect type next to the variable name where we are assigning to.
* Or we can use the so-called **turbofish** operator `::<>()` as we do in the second example.

![](examples/convert/string-to-int/src/main.rs)
![](examples/convert/string-to-int/out.out)

## Convert string to number that ends with newline
{id: rust-convert-string-to-number-end-with-newline}
{i: trim}

![](examples/convert/string-to-int-fail/src/main.rs)
![](examples/convert/string-to-int-fail/out.out)

## Convert string to number after removing whitespaces
{id: rust-convert-string-to-number-trim}
{i: trim}

![](examples/convert/string-to-int-trim/src/main.rs)
![](examples/convert/string-to-int-trim/out.out)

## Convert string to float
{id: convert-string-to-float}
{i: f32}

* Sometimes we are expecting floating point numbers.

![](examples/convert/string-to-float/src/main.rs)
![](examples/convert/string-to-float/out.out)

