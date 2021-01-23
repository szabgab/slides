use strict;
use warnings;

use Test::More;
use Test::Warn;

use MyTools qw(fibo);

subtest negative => sub {
    my $result = 'something else';
    warning_is {$result = fibo(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, undef, 'fibonacci on -1 returns undef');
};

done_testing;
