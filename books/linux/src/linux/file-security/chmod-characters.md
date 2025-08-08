# chmod

* chmod

```
$ touch some_file
$ ls -l some_file
-rw-rw-r-- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod 0 some_file
---------- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod u+rw some_file
-rw------- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod a+x some_file
-rwx--x--x 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod o-x some_file
-rwx--x--- 1 vagrant vagrant 0 Jul  7 14:58 some_file
```


