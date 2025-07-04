use strict;
use warnings;

use MyTools;

use Test::More tests => 2 * 4;

for (1..4) {
    my $value = dice();
    cmp_ok $value, '>', 0, 'bigger than 0';
    cmp_ok $value, '<', 7, 'smaller than 7';
}
