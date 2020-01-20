# Database Testing
{id: database-testing}

## Database testing
{id: manual-database-testing}


This can be considered as part of any application as there is some kind of a database
used by every application. In the simple case the 'database' might be a flat file but
it can also be some csv file or xml file or an RDBMS that you can access using SQL.
In this case you would like to test what are the consequences on the database
of certain operations of the application ?



* Prepare a database
* Execute some code
* Check if the database was updated correctly



## A couple of tools
{id: db-testing-tools}

* [DBI](http://metacpan.org/pod/DBI) - Database independent interface
* DBD::*   Database driver(s)
* [DBIx::Class](http://metacpan.org/pod/DBIx::Class)
* [Test::DatabaseRow](http://metacpan.org/pod/Test::DatabaseRow) - simple database tests



## Test::More and DBI
{id: db-testing-test-more-and-dbi}
![](examples/db/test_dbi.t)


Results:



```
1..4
ok 1 - row received
ok 2 - fname
ok 3 - lname
ok 4 - no more rows
```


## Test::DatabaseRow
{id: db-testing-test-database-row}
![](examples/db/dbrow.t)


Results:



```
1..1
ok 1 - Foo Bar
```



## Test::DatabaseRow fail
{id: db-testing-test-database-row-fail}
![](examples/db/dbrow_fail.t)


The only difference in the test is that we are expecting SZabo instead of Szabo




Results:



```
1..1
not ok 1 - Foo Zorg
#   Failed test 'Foo Zorg'
#   at examples/db/dbrow_fail.t line 15.
# While checking column 'lname' on 1st row
#          got: 'Bar'
#     expected: 'Zorg'
# Looks like you failed 1 test of 1.
```


## Test::DatabaseRow tests more than one row
{id: db-testing-more-than-one-row}
![](examples/db/dbrow_more.t)


Results:



```
1..1
ok 1 - accounts
```


## Test::DatabaseRow tests more than one row - failure
{id: db-testing-more-than-one-row-fail}
![](examples/db/dbrow_more_fail.t)


Results:


![](examples/db/dbrow_more_fail.err)



## Test::DatabaseRow without SQL
{id: db-testing-without-sql}


Of course, writing SQL is not fun, especially if you don't know SQL.
You might prefer to write the logic in Perl and not care about the SQL stuff.


![](examples/db/dbrow_without_sql.t)


Results:



```
1..1
ok 1 - Foo Bar
```






