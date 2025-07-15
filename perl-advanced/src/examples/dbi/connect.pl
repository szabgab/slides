#!/usr/bin/perl
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dsn      = "dbi:SQLite:dbname=$dbfile";
my $user     = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password);

$dbh->disconnect;
