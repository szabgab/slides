# Command line arguments - ARGV
{id: argv}

## Command line arguments - argv
{id: command-line-arguments}
{i: std::env}
{i: argv}
{i: Vec}

* We load the [std::env](https://doc.rust-lang.org/std/env/) module


![](examples/argv/argv.rs)

## Command line program with a single file parameter
{id: command-line-program}
{i: eprintln!}
{i: exit}
{i: std::process::exit}

![](examples/argv/some_tool.rs)

## Rust rectangle ARGV
{id: rectangle-argv}

![](examples/argv/rectangle_argv.rs)

## Exercise: calucaltor argv
{id: exercise-calculator-argv}

Implement a calculator for the 4 basic operations (+, -, /, *) in Rust that accepts the parameters on the command line:

```
rustc calc.rs
./calc 3 + 4
7

./calc 3 - 4
-1
```

* You should not use the rust.sh for this!
* What's going on with multiplication?


## Solution: calucaltor argv
{id: solution-calculator-argv}

![](examples/argv/calc_argv.rs)

