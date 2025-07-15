#!/usr/bin/perl
use strict;
use warnings;

my $filename = "data.txt";

open(my $wfh, '>', $filename) or die;
print $wfh "data";
close $wfh;

open(my $rfh, '<', $filename) or die;
my $line = <$rfh>;
close $rfh;


