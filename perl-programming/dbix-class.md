# Database access using DBIx::Class
{id: perl-dbix-class}





## DBIx::Class
{id: dbix-class}

Use SQL Database without writing SQL




## Create Sample Database
{id: dbix-class-create-sample-database}

{aside}
For our examples we are going to use an SQLite database. It is simple to install
as it comes within DBD::SQLite, its own database driver and it provide everything
we need for our examples.

Actually SQLite is a very good database useful in many applications that don't
require concurrent write access to the database frequently.
{/aside}

In order to create the sample database run `examples/dbi/create_sample.pl`

![](examples/dbix_class/lib/My/DB.pm)




