# Moving over to Test::More


* Test::More

Test::Simple is really a very simple module. Its sole exported function is the "ok" function.

Test::More has the same "ok" function - so it is a drop-in replacement - but it also has lots of
other functions and tools:

* `ok`
* `is`
* `isnt`
* `diag`
* `node`
* `like`
* `cmp_ok`
* `is_deeply`
* `SKIP`
* `TODO`
* `done_testing`
* `subtest`


```
Better error reporting.
```

In the end every test can be based on the single ok() function.
The additional functions mainly serve as convenience methods
to allow better error reporting.



