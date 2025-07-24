use strict;
use warnings;

use MyTools;

use List::MoreUtils qw(any);

use Test::More tests => 4;


for (1..4) {
    my $value = dice();
    ok( (any {$_ eq $value} (1, 2, 3, 4, 5, 6)), 'correct number');
}

