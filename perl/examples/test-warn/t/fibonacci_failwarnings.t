use strict;
use warnings;

use Test::More;
use Test::FailWarnings;
use Test::Warn;

use MyTools qw(fibo);

subtest positive_2 => sub {
    my $result = fibo(2);
    is($result, 1, 'fibonacci on 2');
};

subtest negative => sub {
    my $result;
    warning_is {$result = fibo(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, undef, 'fibonacci on -1 returns undef');
};

subtest positive_4 => sub {
    my $result = fibo(4);
    is($result, 3, 'fibonacci on 4');
};

subtest positive_6 => sub {
    my $result = fibo(6);
    is($result, 8, 'fibonacci on 6');
};

done_testing;
