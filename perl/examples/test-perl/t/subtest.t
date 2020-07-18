use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More;

is sum(1, 1), 2,  '1+1';

subtest negatives => sub {
    is sum(-1, -1), -2, '-1, -1';
    is sum(-1, -1, -1), -3, '-1, -1, -1';
};

is sum(2, 2), 4,  '2+2';

done_testing;

