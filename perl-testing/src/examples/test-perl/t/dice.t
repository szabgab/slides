use strict;
use warnings;

use MyTools;

use Test::More tests => 8;

use lib 't/lib';
use Test::MyTools qw(is_any);


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

