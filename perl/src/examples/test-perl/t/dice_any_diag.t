use strict;
use warnings;

use MyTools;

use List::MoreUtils qw(any);

use Test::More tests => 4;

my @expected = (1, 2, 3, 4, 5, 6);

for (1..4) {
    my $value = dice();
    ok( (any {$_ eq $value} @expected), 'correct number')
        or diag "Received: $value\nExpected:\n" .
            join "", map {"         $_\n"} @expected;
}

