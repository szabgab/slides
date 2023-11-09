# Other
{id: other}

## Variable shadowing
{id: variable-shadowing}
{i: let}

![](examples/other/shadowing/src/main.rs)

## String formatting
{id: string-formatting}
{i: format}
{i: sprintf}

![](examples/other/string-formatting/src/main.rs)

![](examples/other/reverse/src/main.rs)
![](examples/other/reverse/out.out)

![](examples/other/collect/src/main.rs)

## Factorial functions returning Result
{id: factorial-function-returning-result}
{i: Restult}
{i: Ok}
{i: Err}

![](examples/other/factorial-returning-result/src/main.rs)
![](examples/other/factorial-returning-result/out.out)

## Split function into files
{id: split-functions-into-file}

![](examples/other/project/src/main.rs)
![](examples/other/project/src/helper.rs)
![](examples/other/project/Cargo.toml)

## Variable Scope in Rust
{id: rust-variable-scope}

* Every block creates a scope

![](examples/other/scope/src/main.rs)
![](examples/other/scope/out.out)

## Declare empty variable and assign to it later
{id: assign-to-variable-later}

![](examples/other/assign-later/src/main.rs)


## Declare empty variable - requires type
{id: declare-empty-variable}

![](examples/other/empty-string/src/main.rs)
![](examples/other/empty-string/out.out)


## SystemTime now
{id: systemtime-now}

![](examples/other/now/src/main.rs)

## Exit
{id: exit}
{i: exit}

* [Function std::process::exit](https://doc.rust-lang.org/std/process/fn.exit.html)

![](examples/other/exit/src/main.rs)

```
echo $?
echo %ERROR_LEVEL%
```

## Define multiple variables
{id: define-multiple-variables}

![](examples/other/define-multiple-variables/src/main.rs)

## wc
{id: wc}

![](examples/other/rust-wc/Cargo.toml)
![](examples/other/rust-wc/src/main.rs)

## copy vs clone
{id: copy-vs-clone}

TODO
* [What’s the difference between Copy and Clone?](https://doc.rust-lang.org/std/marker/trait.Copy.html#whats-the-difference-between-copy-and-clone)

## Type alias
{id: type-alias}
{i: type}

* We can use the `type` keyword to create aliases to existing types. This can help us in reading the code, but Rust does not do any enforcement.
* As you can see in the following example we can pass arguments to a "different" type as long as it is an alias to the same type.
* [type](https://doc.rust-lang.org/std/keyword.type.html)

![](examples/other/type-alias/src/main.rs)

## Solution: Age limit
{id: solution-age-limit}

![](examples/other/age-limit-18/src/main.rs)
![](examples/other/age-limit-18-21/src/main.rs)
![](examples/other/age-limit-anywhere/src/main.rs)

## Multi-counter in manually handled CSV file
{id: multi-counter-in-manually-handled-csv-file}


![](examples/other/multi_counter_with_manual_csv/src/main.rs)


## Get path to current executable
{id: get-path-to-current-executable}
{i: current_exe}

![](examples/other/current-executable/src/main.rs)

## cache dependencies with sccache
{id: cache-dependencies}

* [sccache](https://github.com/mozilla/sccache)

## Commafy
{id: commafy}

![](examples/other/commafy/Cargo.toml)
![](examples/other/commafy/src/lib.rs)

## Commafys
{id: commafy2}

![](examples/other/commafy2/src/main.rs)


## Use statements
{id: use-statements}

![](examples/other/use-statements/src/main.rs)

## Take version number from Cargo.toml
{id: version-number-from-cargo-toml}
{i: VERSION}
{i: CARGO_PKG_VERSION}


![](examples/other/version-number/src/main.rs)

## Ansi colors
{id: ansi-colors}

* [ansi_term](https://crates.io/crates/ansi_term)

![](examples/other/ansi-colors/Cargo.toml)
![](examples/other/ansi-colors/src/main.rs)

## What I learned from learning Rust
{id: what-i-learned-from-learning-rust}

* Gabor Szabo
* https://szabgab.com/
* https://github.com/szabgab

* https://rustatic.code-maven.com/
* https://rust-digger.code-maven.com/
* https://rust.code-maven.com/

## Temperature converter
{id: tempreature-converter}

![](examples/other/temperature-converter/Cargo.toml)
![](examples/other/temperature-converter/input.json)
![](examples/other/temperature-converter/src/main.rs)

## Check slides
{id: check-slides}

![](examples/other/check-slides/src/main.rs)


## Expressions vs statements
{id: expressions-vs-statement}

* Expressions have a return value do NOT need a trailing semi-colon
* Statements do not have values and need a semi-colon

![](examples/other/statements/src/main.rs)

## Send email via SendGrid
{id: send-email-via-sendgrid}

![](examples/other/send-mail-with-sendgrid/src/main.rs)

![](examples/other/send-mail-with-sendgrid/Cargo.toml)

With a file called config.txt in the same directy that has:

```
SENDGRID_API_KEY=SG....
```

## Compare memory address (pointer)
{id: compare-memory-address}
{i: std::ptr::addr_of}
{i: addr_of}

![](examples/other/compare-memory-address/src/main.rs)
![](examples/other/compare-memory-address/out.out)

## Equality of Some - values
{id: equality-of-some-values}
{i: Some}

![](examples/other/some-equality/src/main.rs)
![](examples/other/some-equality/out.out)


