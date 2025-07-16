#!/usr/bin/perl
use strict;
use warnings;

my $first  = <STDIN>;
chomp $first;
my $other  = <STDIN>;
chomp $other;

if ($first == $other) {
    print "The two numbers are the same\n";
} else {
    print "The two numbers are NOT the same\n";
}

if ($first eq $other) {
    print "The two strings are the same\n";
} else {
    print "The two strings are NOT the same\n";
}

if ($first > $other) {
    print "First is a BIGGER number\n";
} else {
    print "First is a smaller number\n";
}

if ($first gt $other) {
    print "First is a BIGGER string\n";
} else {
    print "First is a smaller string\n";
}
