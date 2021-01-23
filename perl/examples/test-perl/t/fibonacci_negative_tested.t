use strict;
use warnings;

use Test::More;
use Test::Warn;

use MyTools qw(fibo);

subtest negative => sub {
    my $result;
    warning_is {$result = fibo(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, 0, 'fibonacci on -1 returns 0');
};

done_testing;
