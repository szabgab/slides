# Default file permissions: umask

* umask

By default files would be created with permission 0666 which means rw for everyone.


**umask** helps having more secure defaults.


The bits that are set in umask won't be set by the applications.
So if we have umask 0777 then every file will be created without any rights.
If the umask is 0000 then it has no effect and files will be created with 0666.


```
$ umask    to show the current value
$ touch file1
$ ls -l file1

$ umask 0022
$ touch file2
$ ls -l file2
```



