#!/usr/bin/perl
use strict;
use warnings;

use Text::Diff;          # instead of File::Compare


# and diff instead of compare
if (my $diff = diff ("random.log", "regress.log")) {
    print "Regression failed\n\n";
    print $diff;
} else {
    print "Regression successful\n";
}

