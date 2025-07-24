# prove - run other executables

Make prove run tests as executables with no interpreter.  Useful for mixed
language environments and tests written in compiled C.  Just make sure your
tests have the executable bit set and that you're using an unambiguous path to
the test (ie. not "test.t" but "./test.t") so prove doesn't search your $PATH.

```
$ ls -l
total 12K
-rwxrwxr-x 1 schwern schwern 53 2009-02-25 17:30 test.perl
-rwxrwxr-x 1 schwern schwern 53 2009-02-25 17:31 test.ruby
-rwxrwxr-x 1 schwern schwern 42 2009-02-25 17:31 test.sh

$ prove --exec '' t/test.*
t/test.perl....ok
t/test.ruby....ok
t/test.sh......ok
All tests successful.
Files=3, Tests=6,  0 wallclock secs
   ( 0.04 usr  0.02 sys +  0.00 cusr  0.01 csys =  0.07 CPU)
Result: PASS
```


