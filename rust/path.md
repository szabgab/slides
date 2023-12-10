# Path
{id: path}

## Return vector of Path or PathBuf
{id: return-vector-of-path}
{i: Path}
{i: PathBuf}

* We would like to create a function that collectes Path objects and returns them.
* Instead of Path objects we'll return PathBuf objects

![](examples/path/return-pathes/src/main.rs)

## Convert the PathBuf to String to compare
{id: convert-pathbuf-to-string-to-compare}
{i: current_dir}
{i: clone}
{i: into_os_string}
{i: into_string}
{i: unwrap}

![](examples/path/convert-pathbuf-to-string/src/main.rs)

## get file extension
{id: get-file-extension}
{i: Path}
{i: extension}

![](examples/path/get-extension/src/main.rs)

## file extension
{id: file-extension}


![](examples/path/extension/src/main.rs)

```
hello.rs        "rs"
.hello.swp      "swp"
hello.and.swp   "swp"
.github         None
.bashrc         None
dotless         None
```

## parent directory
{id: parent-directory}
{i: parent}
{i: dirname}

* [parent](https://doc.rust-lang.org/std/path/struct.Path.html#method.parent)

![](examples/path/parent/src/main.rs)
![](examples/path/parent/out.out)

## directory ancestors (parent directories)
{id: directory-ancestors}
{i: ancestors}

* [ancestors](https://doc.rust-lang.org/std/path/struct.Path.html#method.ancestors)

![](examples/path/ancestors/src/main.rs)
![](examples/path/ancestors/out.out)

## directory ancestor (n level)
{id: directory-ancestor}
{i: ancestor}
{i: ancestors}
{i: nth}
{i: next}

![](examples/path/ancestor/src/main.rs)
![](examples/path/ancestor/out.out)

## join pathes
{id: join-pathes}
{i: join}

![](examples/path/join/src/main.rs)
![](examples/path/join/out.out)


## basename (file_name)
{id: basename}
{i: file_name}
{i: basename}


![](examples/path/basename/src/main.rs)

