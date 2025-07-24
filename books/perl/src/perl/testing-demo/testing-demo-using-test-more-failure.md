# Testing Demo using Test::More (failure)


{% embed include file="src/examples/testing-demo/t/02-add.t" %}

```
$ prove -l t/02-add.t
```

```
t/02-add.t .. 1/?
#   Failed test at t/02-add.t line 8.
#          got: '6'
#     expected: '5'
# Looks like you failed 1 test of 3.
t/02-add.t .. Dubious, test returned 1 (wstat 256, 0x100)
Failed 1/3 subtests

Test Summary Report
-------------------
t/02-add.t (Wstat: 256 Tests: 3 Failed: 1)
  Failed test:  2
  Non-zero exit status: 1
Files=1, Tests=3,  1 wallclock secs ( 0.01 usr  0.02 sys +  0.04 cusr  0.00 csys =  0.07 CPU)
Result: FAIL
```


