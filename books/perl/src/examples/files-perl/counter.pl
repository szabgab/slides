#!/usr/bin/perl
use strict;
use warnings;

my $filename = "counter.txt";
if (not -e $filename) {
    open my $fh, ">", $filename or die "Could not create counter file: $!";
    print $fh 0;
}

open my $fh, "+<", $filename or die "Could not open counter: $!\n";
my $c = <$fh>;
chomp $c;

seek $fh, 0, 0;
truncate $fh, 0;
$c++;
print $c;

print $fh $c;
close $fh;

