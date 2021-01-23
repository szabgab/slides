use strict;
use warnings;

use Test::More;

use MyTools qw(fibo);

subtest negative => sub {
    my $result = fibo(-1);
    is($result, 0, 'fibonacci on -1 returns 0');
};

done_testing;
