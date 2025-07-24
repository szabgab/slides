#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

my $result;

$result = `$calc 1  + 1`;
if ( $result == 2 ) {
    print "ok\n";
}
else {
    print "not ok\n";
}

$result = `$calc 2 + 2`;
if ( $result == 4 ) {
    print "ok\n";
}
else {
    print "not ok\n";
}

$result = `$calc 2 + 2 + 2`;
if ( $result == 6 ) {
    print "ok\n";
}
else {
    print "not ok\n";
}

# We replaced the "system" calls with backtick in order to catch the STDOUT
# It is extreamly verbose and we are repeating the same code a lot of times

