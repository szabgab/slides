#!/usr/bin/perl 
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dsn      = "dbi:SQLite:dbname=$dbfile";
my $dbh = DBI->connect($dsn);

show_table("before");

my ($email, $id) = ('new@address.com', 1);

$dbh->do("UPDATE people SET email = ? WHERE id = ?", undef, $email, $id);

show_table("after");


sub show_table {
    print "----- $_[0]\n";
    my $sth = $dbh->prepare("SELECT id, email FROM people");
    $sth->execute();
    while (my $h = $sth->fetchrow_hashref('NAME_lc')) {
        print "$h->{id}   $h->{email}\n";
    }
}

