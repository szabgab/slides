#!/usr/bin/perl
use strict;
use warnings;

if (not @ARGV) {
    die "Usage: $0 examples/pair.txt\n";
}

open(my $data, '<', $ARGV[0]) or die "Cannot open $ARGV[0]\n";
my @names = <$data>;
chomp @names;

my @pairs;
foreach (1..@names) {
     my $i = int rand(@names);
     push @pairs, splice(@names, $i, 1);
}


if (@pairs % 2) {
    $alone = shift @pairs;
}
my %pairs = @pairs;
print "ALONE: $alone\n";
foreach $name (sort keys %pairs) {
    print "$name    $pairs{$name}\n";
}

