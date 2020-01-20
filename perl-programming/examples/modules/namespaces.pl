#!/usr/bin/perl
use strict;
use warnings;

package Calc;
use strict;
use warnings;

sub add {
    my $total = 0;
    $total += $_ for (@_);
    return $total;
}


package main;

print Calc::add(3, 4), "\n";

# add(3, 4);
# would die with:
# Undefined subroutine &main::add called
#   at examples\modules\namespaces.pl line 20.