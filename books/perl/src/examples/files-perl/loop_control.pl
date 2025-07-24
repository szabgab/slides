#!/usr/bin/perl
use strict;
use warnings;

my $counter = 0;
my $total = 0;
while (1) {
    $counter++;
    my $num = rand(1);

    # print "Debug: $num  $total\n";

    if ($num < 0.2) {
        next;
    }

    $total += $num;
    if ($total > 3) {
        last;
    }

    ### next jumps here ###
}
### last jumps here ###
print "Counter: $counter Total: $total\n"
