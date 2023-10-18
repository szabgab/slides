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

