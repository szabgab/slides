#!/usr/bin/perl
use strict;
use warnings;

END {
    print "END\n";
}

print "BODY\n";
my $x = 0;
print 1/$x;          # error the program stops working

print "AFTER ERROR\n";

BEGIN {
    print "BEGIN\n";
}

print "After BEGIN block\n";

