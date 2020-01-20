#!/usr/bin/perl
use strict;
use warnings;

sub count {
    if (not defined wantarray) {
        print "ERROR - function called in void context\n";
        return;
    }

    my $count = @_;
    if (not wantarray) {
        #print "SCALAR\n";
        return $count;
    }

    my $sum=0;
    while (my $v = shift @_) {
        $sum += $v;
    }

    #print "ARRAY\n";
    return ($count, $sum);
}

count();                    # call in void context, ERROR message

my (@x) = count(2,3,5);     # LIST context
print "@x\n";               # 3 10

my $z = count(2,3,5);       # SCALAR context
print "$z\n";               # 3
