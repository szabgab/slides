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
    table => 'people',
    where => { '='  => {
                        email => $email, 
                        pw    => $pw,
                        }
            },
    tests => { 'eq' => {
                        fname => 'Foo', 
                        lname => 'Bar',
                        },
            },
    label => 'Foo Bar',
);

$dbh->disconnect;

