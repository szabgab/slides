# Create Sample Database

For our examples we are going to use an SQLite database. It is simple to install
as it comes within DBD::SQLite, its own database driver and it provide everything
we need for our examples.

Actually SQLite is a very good database useful in many applications that don't
require concurrent write access to the database frequently.

In order to create the sample database run `examples/dbi/create_sample.pl`

{% embed include file="src/examples/dbix_class/lib/My/DB.pm" %}


