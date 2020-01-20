#!/usr/bin/env perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);
use DBI          qw();

my $action;
GetOptions("action=s" => \$action);
if (not $action or $action !~ /^(insert|selecta|selecth)$/) {
    print <<"USAGE";
Usage:
      $0 --action insert|selecta|selecth

USAGE
    exit;
}
my $dbfile = "sample.db";

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


sub insert {
    my @people = (
        ['Foo', 'Bar'],
        ['Apple', 'Pie'],
    );
    foreach my $person (@people) {
        $dbh->do("INSERT INTO people (id, fname, lname) VALUES(?, ?, ?)",
            undef,
            1, @$person);
    }
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

