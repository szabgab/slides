package MyDBI;
use base 'Class::DBI';
MyDBI->set_db('Main', 'dbi:SQLite:dbname=site.db');


1;
