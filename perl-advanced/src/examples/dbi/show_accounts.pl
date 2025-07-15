#!/usr/bin/perl 
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dsn      = "dbi:SQLite:dbname=$dbfile";
my $dbh = DBI->connect($dsn);


if ($ARGV[0]) {
    print "----- $ARGV[0]\n";
}

my $sth = $dbh->prepare("SELECT id, amount FROM accounts");
$sth->execute();
while (my $h = $sth->fetchrow_hashref('NAME_lc')) {
    print "$h->{id}   $h->{amount}\n";
}


