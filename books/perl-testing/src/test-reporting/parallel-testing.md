# Parallel testing


```
prove -j4         Run test scripts in parallel
~/.proverc        Can have values like -j4 in it
                  then use -j1 to run sequential
```

* Shared resources? (database, temp files, sockets, etc.)
* Are the test script independent? (setup fixture, teardown in every file.)



