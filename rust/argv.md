# Command line arguments - ARGV
{id: argv}

## Command line arguments - argv
{id: command-line-arguments}
{i: std::env}
{i: argv}
{i: Vec}

* We load the [std::env](https://doc.rust-lang.org/std/env/) module

![](examples/argv/argv/src/main.rs)

```
cargo run

My path is target/debug/argv
Number of arguments is 1
```

```
cargo run apple banana

My path is target/debug/argv
Number of arguments is 3
Parameter 1 is 'apple'
Parameter 2 is 'banana'
```

## Command line program with a single file parameter
{id: command-line-program}
{i: eprintln!}
{i: exit}
{i: std::process::exit}

![](examples/argv/some-tool/src/main.rs)

```
cargo run

Usage: target/debug/some-tool FILENAME
```

```
cargo run data.csv

We are working on file 'data.csv'
```

## Rust rectangle ARGV
{id: rectangle-argv}

![](examples/argv/rectangle-argv/src/main.rs)

```
cargo run

Usage target/debug/rectangle-argv length width
```

```
cargo run  3 4


area: 12
circumference: 14
```

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

![](examples/argv/calc-argv/src/main.rs)

```
cargo run 3 + 4

3 + 4 = 7
```

```
cargo run 3 '*' 4

3 * 4 = 12
```

