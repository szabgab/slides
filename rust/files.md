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
{i: lines}

![](examples/files/read_line_by_line_enumerate.rs)

## Rust - counter
{id: rust-counter}
{i: Read}
{i: Write}
{i: File}
{i: read_to_string}
{i: create}

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
{i: chars}
{i: usize}

![](examples/files/count_digits.rs)

## Makedir
{id: makedir}
{i: mkdir}
{i: create_dir}

* [create_dir](https://doc.rust-lang.org/std/fs/fn.create_dir.html)

![](examples/files/makedir.rs)

## Makedirs
{id: makedirs}
{i: mkdir}
{i: create_dir_all}

* [create_dir_all](https://doc.rust-lang.org/std/fs/fn.create_dir_all.html)

![](examples/files/makedirs.rs)

## Get the temporary directory
{id: get-the-temporary-directory}

![](examples/files/temp_dir.rs)

## Create temporary directory
{id: temporary-directory}

![](examples/files/tempdir-demo/Cargo.toml)
![](examples/files/tempdir-demo/src/main.rs)

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

## Appand to file
{id: append-to-file}

![](examples/files/append.rs)

## Show size of file
{id: show-size-of-file}
{i: size}
{i: len}

![](examples/files/show_size_of_file.rs)

## du - disk usage
{id: du}

![](examples/files/du.rs)

## get file extension
{id: get-file-extension}
{i: Path}
{i: extension}

![](examples/files/get_extension.rs)


## parent directory
{id: parent-directory}
{i: parent}
{i: dirname}

* [parent](https://doc.rust-lang.org/std/path/struct.Path.html#method.parent)

![](examples/files/parent.rs)
![](examples/files/parent.out)

## directory ancestors (parent directories)
{id: directory-ancestors}
{i: ancestors}

* [ancestors](https://doc.rust-lang.org/std/path/struct.Path.html#method.ancestors)

![](examples/files/ancestors.rs)
![](examples/files/ancestors.out)

## directory ancestor (n level)
{id: directory-ancestor}
{i: ancestors}

![](examples/files/ancestor.rs)
![](examples/files/ancestor.out)

## join pathes
{id: join-pathes}
{i: join}

![](examples/files/join.rs)
![](examples/files/join.out)


## basename
{id: basename}

![](examples/files/basename.rs)
