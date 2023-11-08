# Execute and run external commands
{id: external}

## The external program we'll run
{id: the-external-program}

![](examples/external/all/src/main.rs)

Compile:

```
cargo build --relase
```

Run:

```
./target/release/all
./target/release/all 3
```

## Run external programs
{id: run-external-programs}
{i: Command}
{i: from_utf8}
{i: status}
{i: success}
{i: ExitStatus}

* [Command](https://doc.rust-lang.org/std/process/struct.Command.html)

![](examples/external/run-external-command/src/main.rs)
![](examples/external/run-external-command/out.out)

[see](https://stackoverflow.com/questions/41034635/how-do-i-convert-between-string-str-vecu8-and-u8)


