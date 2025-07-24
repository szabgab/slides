use strict;
use warnings;

use Test::More tests => 1;
use Test::Differences;

my @expected = (
    'This is a string',
    'Another string',
);

my @actual = @expected;
$actual[0] .= 'x';

eq_or_diff \@actual, \@expected;

