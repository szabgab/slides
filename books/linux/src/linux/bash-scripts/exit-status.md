# Exit status in $?

* $?

Every command has a so-called exit status. A number between 0-255. 0 indicates success. Other numbers indicate some failure.
The exit status of the last command is always saved in $?

```
$ ls
README      build       examples
$ echo $?
0

$ ls /nosuch
ls: /nosuch: No such file or directory
$ echo $?
1
```



