# Files
{id: files}

## Rust - write to file
{id: rust-write-to-file}
{i: File}
{i: Write}
{i: create}
{i: writeln!}

* [std::fs::File](https://doc.rust-lang.org/std/fs/struct.File.html)
* [std::io::Write](https://doc.rust-lang.org/std/io/trait.Write.html)

![](examples/files/write/src/main.rs)

## Rust - read content of a file as a string
{id: rust-read-content-of-a-file-as-a-string}
{i: open}
{i: read_to_string}

![](examples/files/read-whole-file/src/main.rs)

## Rust - read file line-by-line
{id: rust-read-file-line-by-line}
{i: BufRead}
{i: BufReader}
{i: lines}

![](examples/files/read-line-by-line/src/main.rs)

## Rust - read file line-by-line with row number (enumerate)
{id: rust-read-file-line-by-line-enumerate}
{i: enumerate}
{i: lines}

![](examples/files/read-line-by-line-enumerate/src/main.rs)

## Rust - counter
{id: rust-counter}
{i: Read}
{i: Write}
{i: File}
{i: read_to_string}
{i: create}

![](examples/files/counter/src/main.rs)

## Rust list content of directory
{id: rust-list-directory}
{i: Path}
{i: read_dir}

* [read_dir](https://doc.rust-lang.org/std/path/struct.Path.html#method.read_dir)

![](examples/files/list-dir/src/main.rs)

## Rust list directory content recursively (tree)
{id: directory-tree-recursively}

* std::fs::File [struct.File](https://doc.rust-lang.org/std/fs/struct.File.html)

![](examples/files/tree/src/main.rs)

![](examples/files/list-tree/src/main.rs)

## Count digits in file
{id: count-digits-in-file}
{i: chars}
{i: usize}
{i: enumerate}

![](examples/files/count-digits/src/main.rs)
![](examples/files/count-digits/out.out)

## Makedir
{id: makedir}
{i: mkdir}
{i: create_dir}

* [create_dir](https://doc.rust-lang.org/std/fs/fn.create_dir.html)

![](examples/files/makedir/src/main.rs)

## Makedirs
{id: makedirs}
{i: mkdir}
{i: create_dir_all}

* [create_dir_all](https://doc.rust-lang.org/std/fs/fn.create_dir_all.html)

![](examples/files/makedirs/src/main.rs)

## Get the temporary directory
{id: get-the-temporary-directory}
{i: temp_dir}

![](examples/files/temp-dir/src/main.rs)

## Create temporary directory
{id: temporary-directory}
{i: tempdir}

![](examples/files/tempdir-demo/Cargo.toml)
![](examples/files/tempdir-demo/src/main.rs)

## Current working directory
{id: current-working-directory}
{i: cwd}
{i: pwd}
{i: current_dir}

* [current_dir](https://doc.rust-lang.org/std/env/fn.current_dir.html)

![](examples/files/pwd/src/main.rs)

## Change directory
{id: change-directory}
{i: set_current_dir}
{i: chdir}
{i: cd}


![](examples/files/chdir/src/main.rs)

## open file error handling
{id: open-file-error-handling}

![](examples/files/open-file-handling/src/main.rs)

## Appand to file
{id: append-to-file}
{i: append}
{i: open}

![](examples/files/append/src/main.rs)

## Show size of file
{id: show-size-of-file}
{i: size}
{i: len}

![](examples/files/show-size-of-file/src/main.rs)

## du - disk usage
{id: du}
{i: metadata}
{i: len}
{i: read_dir}

![](examples/files/du/src/main.rs)


