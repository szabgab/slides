use strict;
use warnings;

use Test::More tests => 2;
use Test::Warn;

use lib 'lib';
use MyTools;


{
    my $result;
    warning_is {$result = fibonacci(-1)} "Given number must be > 0",
        'warning when called with -1';
    is($result, 0, 'fibonacci on -1 returns 0');
}

