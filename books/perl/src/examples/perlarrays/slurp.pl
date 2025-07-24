#!/usr/bin/perl
use strict;
use warnings;

my $file = "numbers.txt";
# slurp mode
my $all;
{
    open(my $fh, '<', $file) or die "Could not open '$file'\n";
    local $/ = undef;
    $all = <$fh>;
}


