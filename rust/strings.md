# Strings in Rust
{id: rust-strings}

## Create string
{id: create-string}
{i: println!}

![](examples/strings/create.rs)
![](examples/strings/create.out)

## Length of string
{id: length-of-string}
{i: len}

![](examples/strings/length.rs)
![](examples/strings/length.out)

## Rust - string slices
{id: rust-string-slices}

![](examples/strings/slice.rs)
![](examples/strings/slice.out)

## Rust - string characters
{id: rust-string-character}
{i: chars}

![](examples/strings/characters.rs)
![](examples/strings/characters.out)

## Rust - string ends with
{id: rust-string-ends-with}
{i: ends_with}

![](examples/strings/ends_with.rs)
![](examples/strings/ends_with.out)

## Rust - string starts with
{id: rust-string-starts-with}
{i: starts_with}

![](examples/strings/starts_with.rs)
![](examples/strings/starts_with.out)

## Iterate over the characters of a string
{id: iterate-over-characters}

![](examples/strings/iterate.rs)


## Rust - reverse string
{id: rust-reverse-string}
{i: chars}
{i: rev}
{i: collect}

![](examples/strings/reverse.rs)
![](examples/strings/reverse.out)


## Concatenation str with str
{id: concatetation-str-with-str}

![](examples/strings/concatenation_str_with_str.rs)
![](examples/strings/concatenation_str_with_str.out)

## Concatenation String with String
{id: concatetation-string-with-string}


![](examples/strings/concatenation_string_with_string.rs)
![](examples/strings/concatenation_string_with_string.out)

## Concatenation String with String (clone)
{id: concatetation-string-with-string-clone}
{i: clone}

![](examples/strings/concatenation_string_with_string_clone.rs)
![](examples/strings/concatenation_string_with_string_clone.out)

## Concatenation String with str
{id: concatetation-string-with-str}

![](examples/strings/concatenation_string_with_str.rs)
![](examples/strings/concatenation_string_with_str.out)

## Concatenate strings using format!
{id: concatenate-strings-using-format}
{i: format!}

* In this case all the strings are copied so it is less efficient than where we move the string, but this means we can continue to use the original variables.

![](examples/strings/concatenation_with_format.rs)
![](examples/strings/concatenation_with_format.out)

## concat
{id: concat}
{i: concat}

![](examples/strings/concat.rs)
![](examples/strings/concat.out)

## Split string
{id: split-string}
{i: split}

![](examples/strings/split_string.rs)
![](examples/strings/split_string.out)

## Split string on whitespace
{id: split-string-on-whitespace}
{i: split_whitespace}

![](examples/strings/split_string_whitespace.rs)
![](examples/strings/split_string_whitespace.out)

## Append to string with push_str
{id: append-to-string-with-push-str}
{i: push_str}
{i: to_string}

![](examples/strings/append_to_string.rs)
![](examples/strings/append_to_string.out)

## Create String from literal string using to_string
{id: create-string-from-literal-string}
{i: to_string}

* [ToString](https://doc.rust-lang.org/std/string/trait.ToString.html) is a trait that can convert anything to a String.

![](examples/strings/to_string.rs)
![](examples/strings/to_string.out)

## Str and String equality
{id: str-string-equality}

![](examples/strings/str_string_equality.rs)
![](examples/strings/str_string_equality.out)

## String notes
{id: string-notes}

* str - addr, length (a view into a utf-8 encoded bytes located either in the binary, on the stack, or on the heap)
* &str - borrowed str
* String - addr, length, capacity  (owner)

## String replace all
{id: string-replace}
{i: replace}

![](examples/strings/replace.rs)
![](examples/strings/replace.out)

## String replace limited times
{id: string-replacen}
{i: replacen}

![](examples/strings/replacen.rs)
![](examples/strings/replacen.out)

## String replace range
{id: string-replace-range}
{i: replace_range}


![](examples/strings/replace_range.rs)
![](examples/strings/replace_range.out)


## Function to combine two strings
{id: function-to-combine-two-strings}

![](examples/strings/combine.rs)


## Ownership and strings
{id: ownership-and-strings}

* take ownership

![](examples/strings/take_ownership.rs)

* borrow

![](examples/strings/borrow.rs)

* give ownership

![](examples/strings/give_ownership.rs)

## Slice and change string
{id: slice-and-change-string}

![](examples/strings/slice_and_change.rs)

## To lower, to upper case
{id: to-lowercase}
{i: to_lowercase}
{i: to_uppercase}

![](examples/strings/to_lower_to_upper.rs)

## Compare strings
{id: compare-strings}
{i: cmp}
{i: Less}
{i: Equal}
{i: Greater}
{i: Ordering}

* We can use the regular `<`, `>`, `==` operators to compare both strings and string slices.
* The `cmp` method returns a value from the [Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html) enum.

![](examples/strings/compare-strings/src/main.rs)
![](examples/strings/compare-strings/out.out)


