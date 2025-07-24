# Running External Programs

* system
* ``
* qx

`system()` can execute any external program. You pass to it the same
string as you would type on the command line.

It returns 0 on success and the exit code of the external program on failure.
Hence the strange way we check if it fails.

Passing the program name and the parameters as an array is more secure as it
does not involve invocation of a shell. There is no shell processing involved;


```
system("some_app.exe --option");

```


See perldoc -f system for more error handling

```
my $result = `some_app.exe --option`;
my @result = `some_app.exe --option`;
```

backticks `` are also know as `qx{}`


