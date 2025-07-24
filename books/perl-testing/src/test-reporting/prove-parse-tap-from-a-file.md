# Parse TAP from a file

Prove tricks from Michael G Schwern on the perl-qa list.

Parse TAP from a file, rather than program output.  Handy for doing
experiments without having to mock up a program.

{% embed include file="src/examples/root/foo.tap)

**prove --exec 'cat' examples/root/foo.tap**

```
examples/root/foo.tap .. ok
All tests successful.
Files=1, Tests=2,  0 wallclock secs ( 0.04 usr +  0.01 sys =  0.05 CPU)
Result: PASS
```


