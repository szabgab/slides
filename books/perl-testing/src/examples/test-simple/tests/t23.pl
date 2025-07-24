use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MySimpleCalc qw(sum);

my @tests;
BEGIN {
    @tests = (
        [ 1,  1,  2    ],
        [ 2,  2,  4    ],
        [ 2,  2,  2, 6 ],
        [ 3,  3,  6    ],
        [-1, -1, -2    ],
        [ 1, -1,  0    ],
    );
}

use Test::Simple tests => scalar @tests;

foreach my $t (@tests) {
    my $expected = pop @$t;
    my $real     = sum(@$t);
    my $name     = join " + ", @$t;

    ok( $real == $expected, $name );
}

