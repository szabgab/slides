use strict;
use warnings;

use Test::More;

my @cases = (1, 2, 7);

plan tests => 2 * scalar @cases;

for my $case (@cases) {
    my $value = rand($case);
    cmp_ok $value, '>=', 0, 'bigger than 0';
    cmp_ok $value, '<', $case, "smaller than $case";
}
