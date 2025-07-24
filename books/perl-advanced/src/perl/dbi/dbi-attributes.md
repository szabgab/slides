# Attributes

* attributes|dbi
* AutoCommit
* PrintError
* RaiseError
* NAME_lc
* FetchHashKeyName
* TraceLevel


In addition to the connection string, the username and the password one can
and should configure the database with the DBI specific configuration options
(or attributes).
These options all go in a HASH reference in the 4th parameter of the
DBI connect method.


As the databases and the DBD - Database drivers might all decide
arbitrarily on their mode regarding transactions one should always
explicitly declare how she wants to operate.


The AutoCommit option.

{% embed include file="src/examples/dbi/attributes.pl" %}


