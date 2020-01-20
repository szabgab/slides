#!/usr/bin/perl
use strict;
use warnings;

my $row = <STDIN>;
chomp $row;
print "READ: $row\n";

my @rows = <STDIN>;
chomp @rows;
print "READ " . @rows . " lines\n";


