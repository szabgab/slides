# Architecture of a DBI Application


* dbi
* dbd

{% embed include file="src/examples/dbi/architecture.txt" %}

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


