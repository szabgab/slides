#!/usr/bin/env perl
use strict;
use warnings;

sub add {
    my ($x, $y) = @_;
    return $x+$y;
}

my $add_ref = \&add;

print "$add_ref\n";              # CODE(0x564e85424148)
print &{ $add_ref }(2, 3), "\n"; # 5
print $add_ref->(2, 3), "\n";    # 5

