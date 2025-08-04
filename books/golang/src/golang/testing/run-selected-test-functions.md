# Run selected test functions


At this point you have basically two choices. Assuming you are sure the test is correct, either you can fix the code now,
or you can decide that you delay fixing this code as you have more urgent things to do.



If and when you start fixing the code you will have to run the tests again and again. If you have many tests this can be time consuming.
You might want to run the specific test that is currently failing.  You can do this using the `-run` flag.


Only the TestAdd1:

```
go test -run TestAdd1
```

Only the TestAdd2:

```
go test -run TestAdd2
```

Both:

```
go test -run TestAdd
```

In general you can use regexes to match the names of the test functions you would like to run:

```
go test -run "^(func_test_name)$"
```



