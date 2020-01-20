use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 3;

is sum(1, 1), 2,  '1+1';

subtest negatives => sub {
    plan tests => 2;
    is sum(-1, -1), -2, '-1, -1';
    is sum(-1, -1, -1), -3, '-1, -1, -1';
};

is sum(2, 2), 4,  '2+2';

