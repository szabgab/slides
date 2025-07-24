#!/usr/bin/perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);
use DBI;

my $action;
GetOptions("action=s" => \$action);
if (not $action or $action !~ /^(create|insert|selecta|selecth)$/) {
    print <<"USAGE";
Usage:
      $0 --action create|insert|selecta|selecth

USAGE
    exit;
}
my $dbfile = "sample.db";

if ($action eq "create") {
    create();
    exit;
}

my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile","","", {});
if ($action eq "insert") {
    insert();
}
if ($action eq "selecta") {
    fetch_arrays();
}
if ($action eq "selecth") {
    fetch_hashref();
}


sub create {
    unlink $dbfile if -e $dbfile;
    my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile","","", {});
    $dbh->do("CREATE TABLE people (id INTEGER PRIMARY KEY, fname VARCHAR(100), lname VARCHAR(100))");
    return;
}

sub insert {
    $dbh->do("INSERT INTO people (id, fname, lname) VALUES(?, ?, ?)", undef, 1, "Gabor", "Szabo");
    $dbh->do("INSERT INTO people (id, fname, lname) VALUES(?, ?, ?)", undef, 2, "Josef", "Kiss");
    return;
}

sub fetch_arrays {
    my $sth = $dbh->prepare("SELECT lname, fname FROM people WHERE id = ?");
    $sth->execute(1);
    while (my @result = $sth->fetchrow_array()) {
        print "lname: $result[0], fname: $result[1]\n";
    }
    $sth->finish;
    return;
}

sub fetch_hashref {
    my $sth = $dbh->prepare("SELECT lname, fname FROM people WHERE id = ?");
    $sth->execute(1);
    while (my $result = $sth->fetchrow_hashref("NAME_lc")) {
        print "lname: $result->{lname}, fname: $result->{fname}\n";
    }
    $sth->finish;
    return;
}

