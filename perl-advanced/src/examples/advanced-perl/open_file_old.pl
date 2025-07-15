#!/usr/bin/perl
use strict;
use warnings;

my $filename = "data.txt";

open(FH, ">$filename") or die;
print FH "data";
close FH;

open(FH, $filename) or die;
my $line = <FH>;
close FH;

