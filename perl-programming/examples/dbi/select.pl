#!/usr/bin/perl
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile");


my $sth = $dbh->prepare('SELECT COUNT(*) FROM people');
$sth->execute;

my ($count) = $sth->fetchrow_array();

print "There are $count number of rows.\n";
