use strict;
use warnings;

use MyTools;

use List::MoreUtils qw(any);

use Test::More tests => 8;


for (1..4) {
    my $n = 6;
    my @expected = (1..$n);
    my $value = dice($n);
    is_any($value, \@expected, 'correct number');
}


for (1..4) {
    my $n = 4;
    my @expected = (1..$n);
    my $value = dice($n);
    is_any($value, \@expected, 'correct number');
}


sub is_any {
    my ($actual, $expected, $name) = @_;
    $name ||= '';

    local $Test::Builder::Level = $Test::Builder::Level + 1;
    ok( (any {$_ eq $actual} @$expected), 'correct number')
        or diag "Received: $actual\nExpected:\n" .
            join "", map {"         $_\n"} @$expected;
}

