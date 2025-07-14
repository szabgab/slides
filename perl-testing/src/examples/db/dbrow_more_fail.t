#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 1;
use Test::DatabaseRow;
use DBI;

system "$^X examples/dbi/create_sample.pl";
END { unlink 'sample.db' }

my $dbh = DBI->connect("dbi:SQLite:dbname=sample.db");

local $Test::DatabaseRow::dbh = $dbh;

row_ok( 
    sql   => ['SELECT * FROM accounts'],
    tests => { '>' => { 'amount' => 0 }},
    label => 'accounts',
    results => 3,
    check_all_rows => 1,
);


$dbh->disconnect;


