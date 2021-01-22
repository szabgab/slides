use strict;
use warnings;

use MyTools;

use Test::More tests => 2 * 4;


for (1..4) {
    my $value = dice();
    cmp_ok $value, '>=', 1, 'bigger than 1';
    cmp_ok $value, '<=', 6, 'smaller than 6';
}
