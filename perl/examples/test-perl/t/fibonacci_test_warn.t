use strict;
use warnings;

use Test::More tests => 6;
use Test::Warn;

use lib 'lib';
use MyTools;


{
    my $result;
    warning_is {$result = fibonacci(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, 0, 'fibonacci on -1 returns 0');
}

{
    my $result;
    warning_is {$result = fibonacci(4)} undef, 'no warning here';
    is($result, 3, 'fibonacci on 4 returns 3');
}

{
    my $result;
    warning_is {$result = fibonacci(6)} undef, 'no warning here';
    is($result, 8, 'fibonacci on 6 returns 8');
}


