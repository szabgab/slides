# Create Temporary Directory

* TempDir
* RemoveAll
* rm -rf

{% embed include file="src/examples/tempdir/tempdir.go" %}

{aside}
The `defer os.RemoveAll(tempDir)` will make sure the directory is removed when we exit the program.
{/aside}

* [io/ioutil.TempDir](https://golang.org/pkg/io/ioutil/#TempDir)


