use strict;
use warnings;

use Test::More;

use MyTools qw(fibo);

subtest negative => sub {
    my $result = fibo(-1);
    is($result, undef, 'fibonacci on -1 returns undef');
};

done_testing;
