# Testing Demo for Perl
{id: testing-demo}

## Testing Demo AUT
{id: testing-demo-aut}

AUT = Application under Testing

![](examples/testing-demo/lib/MyMath.pm)

![](examples/testing-demo/bin/add.pl)

![](examples/testing-demo/bin/multiply.pl)

```
perl -I lib add.pl
perl -I lib multiply.pl
```

## Testing Demo using Test::More (success)
{id: testing-demo-using-test-more-success}

```
cpanm Test::More
```

![](examples/testing-demo/t/01-add.t)

```
$ prove -l t/01-add.t
```


```
t/01-add.t .. ok
All tests successful.
Files=1, Tests=1,  0 wallclock secs ( 0.02 usr  0.00 sys +  0.04 cusr  0.00 csys =  0.06 CPU)
Result: PASS
```


## Testing Demo using Test::More (failure)
{id: testing-demo-using-test-more-failure}


![](examples/testing-demo/t/02-add.t)

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

## Testing Demo - Test coverage report
{id: testing-demo-test-coverage-report}


```
cpanm Devel::Cover
```

```
cover -delete
HARNESS_PERL_SWITCHES=-MDevel::Cover prove -l t/01-add.t
cover
```

```
$ cover
Reading database from .../cover_db

------------- ------ ------ ------ ------ ------ ------ ------
File            stmt   bran   cond    sub    pod   time  total
------------- ------ ------ ------ ------ ------ ------ ------
lib/MyMath.pm   84.6    n/a    n/a   80.0    0.0    0.0   75.0
t/01-add.t     100.0    n/a    n/a  100.0    n/a   99.9  100.0
Total           92.5    n/a    n/a   88.8    0.0  100.0   86.8
------------- ------ ------ ------ ------ ------ ------ ------

HTML output written to .../cover_db/coverage.html done.
```

Open `cover_db/coverage.html`.




