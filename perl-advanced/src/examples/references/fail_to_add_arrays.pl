#!/usr/bin/env perl
use strict;
use warnings;

my @left  = (2, 3);
my @right = (7, 8, 5);
add(@left, @right);

sub add {
    my ($first, $second) = @_;
    print "$first\n";
    print "$second\n";
}

# 2
# 3

addx(@left, @right);
sub addx {
    my (@first, @second) = @_;
    print "First: @first\n";
    print "Second: @second\n";
}

# First: 2 3 7 8 5
# Second:

