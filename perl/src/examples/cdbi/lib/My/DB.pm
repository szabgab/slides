package My::DB;
use strict;
use warnings;

use base 'Class::DBI';
__PACKAGE__->set_db('Main', 'dbi:SQLite:dbname=sample.db');


1;
