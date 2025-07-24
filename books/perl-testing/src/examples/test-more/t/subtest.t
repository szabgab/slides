use strict;
use warnings;

use MySimpleCalc qw(sum);

use Test::More;

subtest positives => sub {
    is sum(1, 1), 2,  '1+1';
    is sum(2, 2), 4,  '2+2';
};

subtest negatives => sub {
    is sum(-1, -1), -2, '-1, -1';
    is sum(-1, -1, -1), -3, '-1, -1, -1';
};

done_testing;

