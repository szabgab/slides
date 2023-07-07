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

## Rust and print
{id: rust-and-print}

```
print!
println!
eprint!   to STDERR
eprintln! to STDERR

format!
```

## Macros
{id: macros}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* Metaprogramming - a program that generate a program

## Split function into files
{id: split-functions-into-file}

![](examples/project/src/main.rs)
![](examples/project/src/helper.rs)
![](examples/project/Cargo.toml)
![](examples/project/Cargo.lock)

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

![](examples/serde-demo/Cargo.lock)
![](examples/serde-demo/Cargo.toml)

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

![](examples/simple_logger_demo/Cargo.lock)
