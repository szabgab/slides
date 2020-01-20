#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 1;
use Test::DatabaseRow;
use DBI;

system "$^X examples/dbi/create_sample.pl";
END { unlink 'sample.db' }

my ($email, $pw) = ('foo@bar.com', 'secret');

my $dbh = DBI->connect("dbi:SQLite:dbname=sample.db");

local $Test::DatabaseRow::dbh = $dbh;

row_ok( 
    sql   => ['SELECT * FROM people WHERE email=? AND pw=?', $email, $pw],
    tests => [ fname => 'Foo', lname => 'Zorg'],
    label => "Foo Zorg",
);


$dbh->disconnect;


