#!/usr/bin/perl
use strict;
use warnings;

use FindBin qw($Bin);
use DBI;

my $verbose = shift;

my $dbfile = "sample.db";

unlink $dbfile;

print "Creating sample SQLite database at $dbfile\n" if $verbose;
my $dbh = DBI->connect("dbi:SQLite:dbname=sample.db");

my $schema;
{
    open my $fh, '<', "$Bin/sample.sql" or die;
    local $/ = undef;
    $schema = <$fh>;
}
foreach my $sql (split /;/, $schema) {
    next if $sql !~ /\S/; # skip empty entries
    $dbh->do($sql);
}
$dbh->disconnect;


