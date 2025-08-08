# file tests

* -e
* -f
* -d
* -e

{% embed include file="src/examples/script/file_tests.sh" %}

```
$ ./examples/script/file_tests.sh
Usage ./examples/script/file_tests.sh FILE

$ ./examples/script/file_tests.sh abc
abc does NOT exist

$ ./examples/script/file_tests.sh .
. if a directory

$ ./examples/script/file_tests.sh examples/script/file_tests.sh
examples/script/file_tests.sh if a file
```

The spaces inside the square brackets are significant.


```
-e    thing exists
-f    thing is a file
-d    thing is a directory
-L    thing is a symbolic link
-s    thing is not empty
...
-r    thing is readable by current user
-w    thing is writable by current user
-x    thing is executable by current user
```



