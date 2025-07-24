# Debugging (Trace levels)

```perl
$dbh->trace();
$sth->trace();
DBI->trace();

TraceLevel attribute

Can be used like this:

DBI->trace(1);
DBI->trace(1, '/tmp/dbitrace.log');

The trace level can be 0 (off) .. 15 (usually 1-4 is more than enough)

In CGI scripts add the following:
BEGIN { $ENV{DBI_TRACE}='1=/tmp/dbitrace.log'; }
```

[Calculating bank balance, take two: DBD::CSV](https://perlmaven.com/calculate-bank-balance-take-two-dbd-csv)


