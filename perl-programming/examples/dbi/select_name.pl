#!/usr/bin/perl
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile");


my $sth = $dbh->prepare('SELECT fname, lname FROM people');
$sth->execute;

while (my @row = $sth->fetchrow_array()) {
    print "$row[0] $row[1]\n";
}

