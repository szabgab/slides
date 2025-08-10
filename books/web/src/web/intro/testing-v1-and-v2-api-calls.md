# Testing the v1 and v2 API calls

Copy t/v1.t to t/v2.t  and add two lines testing the Access-Control-Allow-Origin header and the lack of it.


```
subtest v1_greeting => sub {
    my $res  = $test->request( GET '/api/v1/greeting' );
    ...
    is $res->header('Access-Control-Allow-Origin'), undef;
}
```

```
subtest v2_greeting => sub {
    my $res  = $test->request( GET '/api/v2/greeting' );
    ...
    is $res->header('Access-Control-Allow-Origin'), '*';
}
```

```
perl Makefile.PL
make
make test
```




