#!/usr/bin/perl 
use strict;
use warnings;


my @letters = qw(a b c d e f g h);
print "@letters\n";              # a b c d e f g h
print "$letters[3]\n";           # d   the element with index 3
print "@letters[3]\n";           # d   (a one element array !)
   # generates a warning:
   # Scalar value @letters[3] better written as $letters[3]
   # at examples/advanced/array_slices.pl line 9.

my @data1 = ($letters[3], $letters[2]);        # d c
print "@data1\n";

my @data2 = @letters[3, 2];                    # d c
print "@data2\n";        # d c

print "@letters[3..5]\n";        # d e f
print "@letters[3,3,2]\n";       # d d c

