#!/usr/bin/perl
use strict;
use warnings;

my $val;
print defined $val ? "defined\n" : "not defined\n";   # not defined

$val //= 42;

print "$val\n";   # 42



$val = 0;

print "$val\n";   # 0

$val //= 42;

print "$val\n";   # 0
