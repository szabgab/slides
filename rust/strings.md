# Strings in Rust
{id: rust-strings}

## Create string
{id: create-string}
{i: println!}
{i: String}
{i: from}
{i: to_string}
{i: to_owned}

* The first one is a reference to a string embedded in the program. You can never change this.
* `String::from` and [to_string](https://doc.rust-lang.org/std/string/trait.ToString.html) trait

![](examples/strings/create/src/main.rs)
![](examples/strings/create/out.out)

## Length of string
{id: length-of-string}
{i: len}

* With the `len` method we can get the length of a string in bytes.

![](examples/strings/length/src/main.rs)
![](examples/strings/length/out.out)

## Rust - string slices
{id: rust-string-slices}

![](examples/strings/slice/src/main.rs)
![](examples/strings/slice/out.out)

## Rust - string characters
{id: rust-string-character}
{i: chars}

![](examples/strings/characters/src/main.rs)
![](examples/strings/characters/out.out)

## Rust - string ends with
{id: rust-string-ends-with}
{i: ends_with}

![](examples/strings/ends-with/src/main.rs)
![](examples/strings/ends-with/out.out)

## Rust - string starts with
{id: rust-string-starts-with}
{i: starts_with}

![](examples/strings/starts-with/src/main.rs)
![](examples/strings/starts-with/out.out)

## Iterate over the characters of a string
{id: iterate-over-characters}
{i: chars}

![](examples/strings/iterate/src/main.rs)
![](examples/strings/iterate/out.out)


## Rust - reverse string
{id: rust-reverse-string}
{i: chars}
{i: rev}
{i: collect}

![](examples/strings/reverse/src/main.rs)
![](examples/strings/reverse/out.out)


## Concatenation str with str
{id: concatetation-str-with-str}

![](examples/strings/concatenation-str-with-str/src/main.rs)
![](examples/strings/concatenation-str-with-str/out.out)

## Concatenation String with String
{id: concatetation-string-with-string}


![](examples/strings/concatenation-string-with-string/src/main.rs)
![](examples/strings/concatenation-string-with-string/out.out)

## Concatenation String with String (clone)
{id: concatetation-string-with-string-clone}
{i: clone}

![](examples/strings/concatenation-string-with-string-clone/src/main.rs)
![](examples/strings/concatenation-string-with-string-clone/out.out)

## Concatenation String with str
{id: concatetation-string-with-str}

![](examples/strings/concatenation-string-with-str/src/main.rs)
![](examples/strings/concatenation-string-with-str/out.out)

## Concatenate strings using format!
{id: concatenate-strings-using-format}
{i: format!}

* In this case all the strings are copied so it is less efficient than where we move the string, but this means we can continue to use the original variables.

![](examples/strings/concatenation-with-format/src/main.rs)
![](examples/strings/concatenation-with-format/out.out)

## concat
{id: concat}
{i: concat}

![](examples/strings/concat/src/main.rs)
![](examples/strings/concat/out.out)

## Split string
{id: split-string}
{i: split}

![](examples/strings/split-string/src/main.rs)
![](examples/strings/split-string/out.out)

## Split string on whitespace
{id: split-string-on-whitespace}
{i: split_whitespace}

![](examples/strings/split-string-whitespace/src/main.rs)
![](examples/strings/split-string-whitespace/out.out)

## Append to string with push_str
{id: append-to-string-with-push-str}
{i: push}
{i: push_str}
{i: to_string}

![](examples/strings/append-to-string/src/main.rs)
![](examples/strings/append-to-string/out.out)

## Create String from literal string using to_string
{id: create-string-from-literal-string}
{i: to_string}

* [ToString](https://doc.rust-lang.org/std/string/trait.ToString.html) is a trait that can convert anything to a String.

![](examples/strings/to-string/src/main.rs)
![](examples/strings/to-string/out.out)

## Str and String equality
{id: str-string-equality}

![](examples/strings/str-string-equality/src/main.rs)
![](examples/strings/str-string-equality/out.out)

## String notes
{id: string-notes}

* str - addr, length (a view into a utf-8 encoded bytes located either in the binary, on the stack, or on the heap)
* &str - borrowed str
* String - addr, length, capacity  (owner)

## String replace all
{id: string-replace}
{i: replace}

![](examples/strings/replace/src/main.rs)
![](examples/strings/replace/out.out)

## String replace limited times
{id: string-replacen}
{i: replacen}

![](examples/strings/replacen/src/main.rs)
![](examples/strings/replacen/out.out)

## String replace range
{id: string-replace-range}
{i: replace_range}


![](examples/strings/replace-range/src/main.rs)
![](examples/strings/replace-range/out.out)


## Function to combine two strings
{id: function-to-combine-two-strings}

![](examples/strings/combine/src/main.rs)
![](examples/strings/combine/out.out)


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


