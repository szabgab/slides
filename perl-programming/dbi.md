# Advanced Database access using Perl DBI
{id: perl-advanced-dbi}


## Data integrity
{id: dbi-data-integrity}


When you are working in a place where data integrity is important you have
to use transactions when executing multiple queries that should either all
succeed or all fail.


![](examples/dbi/integrity_loss.pl)


Try to see what happens when you enable the exit() function


![](examples/dbi/show_accounts.pl)



## Transactions
{id: dbi-transaction}
{i: transactions}
{i: begin_work}
{i: commit}
{i: rollback}

```
$dbh->begin_work
$dbh->commit
$dbh->rollback
```
![](examples/dbi/transaction.pl)



## Sample database creation
{id: dbi-sample-database}
![](examples/dbi/create_sample.pl)



## Disconnect from the database
{id: dbi-disconnect}
{i: disconnect}

```
$dbh->disconnect
```



## Attributes
{id: dbi-attributes}
{i: attributes|dbi}
{i: AutoCommit}
{i: PrintError}
{i: RaiseError}
{i: NAME_lc}
{i: FetchHashKeyName}
{i: TraceLevel}

{aside}

In addition to the connection string, the username and the password one can 
and should configure the database with the DBI specific configuration options
(or attributes).
These options all go in a HASH reference in the 4th parameter of the 
DBI connect method.
{/aside}


{aside}

As the databases and the DBD - Database drivers might all decide 
arbitrarily on their mode regarding transactions one should always
explicitly declare how she wants to operate.
{/aside}


{aside}

The AutoCommit option.
{/aside}

![](examples/dbi/attributes.pl)


## Error handling
{id: dbi-error-handling}

* Set the attributes PrintError and RaiseError
* Check for returned undef (or empty lists)
* Check $h->err   and $h->errstr (aka. $DBI::err and $DBI::errstr)
* err    - Native DB engine error code
* errstr - Native DB engine error string

![](examples/dbi/error_handling.pl)



fetchrow_array (and others) return undef when no more row or if
they encounter an error. Use RaiseError or check $sth->err




## Debugging (Trace levels)
{id: dbi-debugging}

```
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

