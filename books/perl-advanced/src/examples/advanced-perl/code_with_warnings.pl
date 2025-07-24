#!/usr/bin/perl 
use strict;
use warnings;

my $total;

add();

print "$total\n";


sub add {
    $total = $total + rand();
}

# triggers:
# Use of uninitialized value in addition (+)
#   at examples/advanced/code_with_warnings.pl line 14.
# or in 5.10
# Use of uninitialized value $total in addition (+)
#   at examples/advanced/code_with_warnings.pl line 14.
