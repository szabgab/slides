# Other
{id: other}

## Variable shadowing
{id: variable-shadowing}
{i: let}

![](examples/other/shadowing.rs)

## String formatting
{id: string-formatting}
{i: format}
{i: sprintf}

![](examples/intro/string_formatting.rs)

![](examples/functions/reverse.rs)
![](examples/functions/square_root.rs)
![](examples/other/collect.rs)

## Macros
{id: macros}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* Metaprogramming - a program that generate a program

## Split function into files
{id: split-functions-into-file}

![](examples/project/src/main.rs)
![](examples/project/src/helper.rs)
![](examples/project/Cargo.toml)

## Variable Scope in Rust
{id: rust-variable-scope}

* Every block creates a scope

![](examples/intro/scope.rs)
![](examples/intro/scope.out)

## Declare empty variable and assign to it later
{id: assign-to-variable-later}

![](examples/other/assign_later.rs)


## Declare empty variable - requires type
{id: declare-empty-variable}

![](examples/intro/empty_string.rs)
![](examples/intro/empty_string.out)


## SystemTime now
{id: systemtime-now}

![](examples/other/now.rs)

## serde
{id: serde}

![](examples/serde-demo/Cargo.toml)
![](examples/serde-demo/src/main.rs)

## serde manipulate json (change, add)
{id: serde-manipulate-json}

![](examples/serde-manipulate-json/Cargo.toml)
![](examples/serde-manipulate-json/src/main.rs)

## Exit
{id: exit}
{i: exit}

* [Function std::process::exit](https://doc.rust-lang.org/std/process/fn.exit.html)

![](examples/other/exit.rs)

```
echo $?
echo %ERROR_LEVEL%
```

## Logging
{id: logging}

![](examples/simple_logger_demo/Cargo.toml)

![](examples/simple_logger_demo/src/main.rs)

## Define multiple variables
{id: define-multiple-variables}

![](examples/other/define_multiple_variables.rs)

## wc
{id: wc}

![](examples/rust-wc/Cargo.toml)
![](examples/rust-wc/src/main.rs)

## copy vs clone
{id: copy-vs-clone}

TODO
* [What’s the difference between Copy and Clone?](https://doc.rust-lang.org/std/marker/trait.Copy.html#whats-the-difference-between-copy-and-clone)

## Run external programs
{id: run-external-programs}

* [Command](https://doc.rust-lang.org/std/process/struct.Command.html)

![](examples/external/all.rs)

```
rustc all.rs
```

![](examples/external/run_external_command.rs)

[see](https://stackoverflow.com/questions/41034635/how-do-i-convert-between-string-str-vecu8-and-u8)

## Type alias
{id: type-alias}
{i: type}

* We can use the `type` keyword to create aliases to existing types. This can help us in reading the code, but Rust does not do any enforcement.
* As you can see in the following example we can pass arguments to a "different" type as long as it is an alias to the same type.
* [type](https://doc.rust-lang.org/std/keyword.type.html)

![](examples/other/type_alias.rs)

## Solution: Age limit
{id: solution-age-limit}

![](examples/other/age_limit_18.rs)
![](examples/other/age_limit_18_21.rs)
![](examples/other/age_limit_anywhere.rs)

## Multi-counter in manually handled CSV file
{id: multi-counter-in-manually-handled-csv-file}


![](examples/multi_counter_with_manual_csv/src/main.rs)


## Get path to current executable
{id: get-path-to-current-executable}
{i: current_exe}

![](examples/other/current_executable.rs)

## cache dependencies with sccache
{id: cache-dependencies}

* [sccache](https://github.com/mozilla/sccache)

