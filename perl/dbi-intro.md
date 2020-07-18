# Database access using Perl DBI
{id: perl-dbi}


## Architecture of a DBI Application
{id: dbi-architecture}
{i: dbi}
{i: dbd}

![](examples/dbi/architecture.txt)

```
Any number of databases at the same time.
Probably every RDBMS can be accessed with its own DBD.
```

While in many areas Perl has plenty of ways to achieve things in the area of database
access a single package has evolved as the de-facto standard way of the low level access.
The DBI - Database Independent Interface of Perl - is the module that most of the perl
applications in the world use as their core.

Between this module and between virtually and relational database we have a Database Driver -
a module in the `DBD::*` namespace. For example there are modules such as DBD::Oracle and DBD::MySQL
or DBD::Pg for PostgreSQL.

Above DBI there are hundreds of higher level abstractions. Most of them live in the `DBIx::*`
namespace on CPAN.


## Create Sample Database
{id: dbi-create-sample-database}
{i: sqlite}


For our examples we are going to use an SQLite database. It is simple to install
as it comes within DBD::SQLite, its own database driver and it provides everything
we need for our examples.

Actually SQLite is a very good database useful in many applications that don't
require concurrent write access to the database frequently.

In order to create the sample database run `examples/dbi/create_sample.pl`

![](examples/dbi/sample.sql)


## Connect to database
{id: dbi-connect-to-database}
{i: connect}

![](examples/dbi/connect.pl)

```
Connecting to other databases:

my $dsn = "DBI:mysql:database=$database;host=$hostname;port=$port";
my $dbh = DBI->connect($dsn, $user, $password);

```


## SELECT with one result
{id: dbi-select-with-one-result}
{i: SELECT}

![](examples/dbi/select.pl)


## SELECT with more results
{id: dbi-select-with-more-results}

![](examples/dbi/select_name.pl)


## SELECT, prepare with placeholders
{id: dbi-select-prepare-with-placeholders}
{i: placeholder}

![](examples/dbi/select_with_placeholders.pl)


## SELECT, using hashref
{id: dbi-select-using-hashref}
{i: NAME_lc}

![](examples/dbi/select_hashref.pl)


## INSERT
{id: dbi-insert}
{i: INSERT}

![](examples/dbi/insert.pl)

We might need to insert some data.


## UPDATE
{id: dbi-update}
{i: UPDATE}

![](examples/dbi/update.pl)
![](examples/dbi/update.out)

We might need to update some data.

The same can be also done using a prepared a statement. It is better to use prepared
statements if you would like to execute the same SQL query several times with different
values.

[Simple Database access using Perl DBI and SQL](https://perlmaven.com/simple-database-access-using-perl-dbi-and-sql)

