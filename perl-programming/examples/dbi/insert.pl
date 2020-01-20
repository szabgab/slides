#!/usr/bin/perl
use strict;
use warnings;

use DBI;

my $dbfile = "sample.db";

my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile");

my ($fname, $lname, $email, $pw) = qw(Moose Foobar moose@foobar.com really?);


$dbh->do('INSERT INTO people (fname, lname, email, pw) VALUES (?, ?, ?, ?)',
            undef, 
            $fname, $lname, $email, $pw);
