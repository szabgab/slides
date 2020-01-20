#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 4;
use DBI;

system "$^X examples/dbi/create_sample.pl";
END { unlink 'sample.db' }

my $email = 'foo@bar.com';
my $pw    = 'secret'; 

my $dbh = DBI->connect("dbi:SQLite:dbname=sample.db");
my $sth = $dbh->prepare('SELECT * FROM people WHERE email=? AND pw=?');
$sth->execute($email, $pw);

my $h = $sth->fetchrow_hashref('NAME_lc');
ok($h, "row received");
is($h->{fname}, 'Foo', 'fname');
is($h->{lname}, 'Bar', 'lname');

$h = $sth->fetchrow_hashref('NAME_lc');
ok(!$h, "no more rows");

$dbh->disconnect;

