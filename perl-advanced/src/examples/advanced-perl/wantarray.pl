#!/usr/bin/perl
use strict;
use warnings;

sub f {
    if (not defined wantarray()) {
        print "called in VOID context\n";
    } elsif (wantarray()) {
        print "called in LIST context\n";
    } else {
        print "called in SCALAR context\n";
    }
}

f();          # called in VOID context
my @y = f();  # called in LIST context
my $x = f();  # called in SCALAR context
