use strict;
use warnings;

use lib 'lib';
use MySimpleCalcFixed qw(sum);

use Test::More tests => 3;

diag "Add two numbers";
is(sum(1, 1),    2,     '1+1');
is(sum(2, 2),    4,     '2+2');

diag "Add 3 numbers";
TODO: {
    local $TODO = "fix bug summing more than 2 values";
    is(sum(2, 2, 2), 6,  '2+2+2');
}

