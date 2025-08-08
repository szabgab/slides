# free

* free

Show free memory.


```
$ free -ht
             total       used       free     shared    buffers     cached
Mem:          3.9G       3.8G        32M        96K        97M       1.1G
-/+ buffers/cache:       2.6G       1.2G
Swap:         1.0G        61M       962M
Total:        4.9G       3.9G       995M
```

* total - physical memory
* cached - memory used to speed up operations. e.g. file read-write operations. This can be used by an application.
* buffers - Temporary memory to help some processes. (e.g. file meta data).
* In the first line  used includes buffers + cached.
* In the second line used only includes memory used by applications.



