# Testing Demo - Test coverage report

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



