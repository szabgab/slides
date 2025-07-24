use strict;
use warnings;
use 5.010;

BEGIN {
    my @values = (0.03, 0.72);
    *CORE::GLOBAL::rand = sub {
        return shift @values;
    };
}

use Test::More;
use MyRandomApp qw(dice);


is dice(10), 1;
is dice(10), 8;

my $x = rand;
is $x, undef, 'We have replaced rand here too';

done_testing;
