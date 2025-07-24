#!/usr/bin/env perl
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

unlink $dbfile if -e $dbfile;
my $sql = <<'SCHEMA';
CREATE TABLE people (
   id INTEGER PRIMARY KEY,
   fname VARCHAR(100),
   lname VARCHAR(100)
);
SCHEMA

my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile","","", {});
$dbh->do($sql);

