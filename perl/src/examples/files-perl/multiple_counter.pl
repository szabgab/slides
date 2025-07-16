#!/usr/bin/perl
use strict;
use warnings;

unless (@ARGV) {
    print "Usage: $0 <counter-id>\n";
    exit;
}

my $id = shift @ARGV;
$id--;               # because we index the counters from 1 and the array is from 0

my $filename = "multiple_counter.txt";
if (not -e $filename) {
    open my $fh, ">", $filename or die "Could not create counter file: $!";
    print $fh 0;
}

open my $fh, "+<", $filename or die "Could not open counter: $!\n";
my @c = <$fh>;
chomp @c;

seek $fh, 0, 0;   # move to the beginning of the file 
truncate $fh, 0;  # cut the file to a certain size

$c[$id]++;
print $c[$id];

foreach my $v (@c) {
    if (defined $v) {
            print $fh "$v\n";
    } else {
        print $fh "\n"; 
    }
}
close $fh;

