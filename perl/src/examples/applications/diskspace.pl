#!/usr/bin/env perl
use strict;
use warnings;

use Filesys::DfPortable qw(dfportable);

#my $df = dfportable("/", 1024 * 1024 * 1024);

my $df = dfportable("/", 1024);
print "Total Size:             $df->{blocks} K\n";
print "Available:              $df->{bfree} K\n";
print "Used:                   $df->{bused} K\n";
print "Percent Full:           $df->{per} %\n";
print "Total available to me:  $df->{bavail} K\n";

