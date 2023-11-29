# Command line arguments - ARGV
{id: argv}

## Command line arguments - argv
{id: command-line-arguments}
{i: std::env}
{i: argv}
{i: Vec}

* We load the [std::env](https://doc.rust-lang.org/std/env/) module
* `#[allow(clippy::needless_range_loop)]` is needed to silence clippy, the linter

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

## Default value on the command line
{id: default-value-for-argv}

* In this example we set the `config_file` variable to the parameter passed on the command line
* or to a default value that can be any string, including the empty string.

![](examples/argv/default-value/src/main.rs)


## Default path - return PathBuf
{id: return-pathbuf}
{i: PathBuf}
{i: args}

* The user must supply the path to root and optionally the path to the pages.
* If the user does not supply the path to the pages then we use root/pages

![](examples/argv/default-path/src/main.rs)

Returning the second parameter as the path to pages:

```
$ cargo run one two

root: one
page: "two"
```

Returning root/pages:

```
$ cargo run one
root: one
page: "one/pages"
```



