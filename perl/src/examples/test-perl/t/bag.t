use strict;
use warnings;

use Test::More tests => 2;
use Test::Deep;


{
    my @expected = (1, 2, 3);
    my @received = (3, 1, 2);
    cmp_bag(\@received, \@expected);
}

{
    my @expected = ([1, 'a'], [2, 'b'], [3, 'c']);
    my @received = ([3, 'c'], [1, 'a'], [2, 'b']);
    cmp_bag(\@received, \@expected);
}


