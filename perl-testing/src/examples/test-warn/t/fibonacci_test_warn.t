use strict;
use warnings;

use Test::More;
use Test::Warn;

use MyTools qw(fibo);

subtest negative => sub {
    my $result;
    warning_is {$result = fibo(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, undef, 'fibonacci on -1 returns undef');
};

subtest positive_4 => sub {
    my $result;
    warning_is {$result = fibo(4)} undef, 'no warning here';
    is($result, 3, 'fibonacci on 4 returns 3');
};

subtest positive_6 => sub {
    my $result;
    warning_is {$result = fibo(6)} undef, 'no warning here';
    is($result, 8, 'fibonacci on 6 returns 8');
};

done_testing;
