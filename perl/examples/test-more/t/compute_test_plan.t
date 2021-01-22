use strict;
use warnings;

use Test::More tests => 2 * 4;

for (1..4) {
    my $value = rand(2);
    cmp_ok $value, '>=', 0, 'bigger than 0';
    cmp_ok $value, '<', 2, 'smaller than 2';
}
