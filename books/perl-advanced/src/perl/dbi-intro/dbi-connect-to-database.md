# Connect to database


* connect

{% embed include file="src/examples/dbi/connect.pl" %}

Connecting to other databases:

```perl
my $dsn = "DBI:mysql:database=$database;host=$hostname;port=$port";
my $dbh = DBI->connect($dsn, $user, $password);

```


