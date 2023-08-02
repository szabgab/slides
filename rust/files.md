# Files
{id: files}

## Rust - write to file
{id: rust-write-to-file}
{i: File}
{i: Write}
{i: create}
{i: writeln!}

![](examples/files/write.rs)

## Rust - read content of a file as a string
{id: rust-read-content-of-a-file-as-a-string}
{i: open}
{i: read_to_string}

![](examples/files/read_whole_file.rs)

## Rust - read file line-by-line
{id: rust-read-file-line-by-line}
{i: BufRead}
{i: BufReader}
{i: lines}

![](examples/files/read_line_by_line.rs)

## Rust - read file line-by-line with row number (enumerate)
{id: rust-read-file-line-by-line-enumerate}
{i: enumerate}

![](examples/files/read_line_by_line_enumerate.rs)

## Rust - counter
{id: rust-counter}

![](examples/files/counter.rs)

## Rust list content of directory
{id: rust-list-directory}
{i: Path}
{i: read_dir}

* [read_dir](https://doc.rust-lang.org/std/path/struct.Path.html#method.read_dir)

![](examples/files/list_dir.rs)

## Rust list directory content recursively (tree)
{id: directory-tree-recursively}

* std::fs::File [struct.File](https://doc.rust-lang.org/std/fs/struct.File.html)

![](examples/files/tree.rs)

![](examples/files/list_tree.rs)

## Count digits in file
{id: count-digits-in-file}

![](examples/files/count_digits.rs)

## Makedirs
{id: makedirs}

![](examples/files/makedir.rs)

## Get the temporary directory
{id: get-the-temporary-directory}

![](examples/files/temp_dir.rs)

## Create temporary directory
{id: temporary-directory}

![](examples/tempdir-demo/Cargo.toml)
![](examples/tempdir-demo/src/main.rs)

## Current working directory
{id: current-working-directory}
{i: cwd}
{i: pwd}
{i: current_dir}

* [current_dir](https://doc.rust-lang.org/std/env/fn.current_dir.html)

![](examples/files/pwd.rs)

## Change directory
{id: change-directory}
{i: set_current_dir}
{i: chdir}
{i: cd}

![](examples/files/chdir.rs)

## open file error handling
{id: open-file-error-handling}

![](examples/files/open_file_handling.rs)

