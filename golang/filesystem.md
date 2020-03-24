# Filesystem
{id: filesystem}


## os.stat information about a file or directory (file exists)
{id: os-stat}
{i: os}
{i: IsNotExist}
{i: Stat}

![](examples/file-stat/stat.go)

```
Error: stat hello/world: no such file or directory
```

If the directory where the file can be found is not executable by the user who runs this code, we'll get
the following error:

```
Error: stat hello/world: permission denied
```

## List Directory
{id: list-directory}
{i: ioutil}
{i: ReadDir}

![](examples/list_directory/listdir.go)


## Get Current Working Directory (cwd)
{id: get-current-working-directory}
{i: cwd}
{i: pwd}
{i: Getcwd}

![](examples/cwd/cwd.go)

* [os.Getwd](https://golang.org/pkg/os/#Getwd)

## Create Temporary Directory
{id: create-temporary-directory}
{i: TempDir}
{i: RemoveAll}
{i: rm -rf}

![](examples/tempdir/tempdir.go)

{aside}
The `defer os.RemoveAll(tempDir)` will make sure the directory is removed when we exit the program.
{/aside}

* [io/ioutil.TempDir](https://golang.org/pkg/io/ioutil/#TempDir)


## Traverse directory tree
{id: traverse-directory-tree}


![](examples/dirtree/tree.go)

* [path/filepath.Walk](https://golang.org/pkg/path/filepath/#Walk)

