use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 3;

diag "Add two numbers";

is(sum(1, 1),    2,     '1+1');
is(sum(2, 2),    4,     '2+2');

diag "Add 3 numbers";
note "We have a bug here, we cannot add more than 2 numbers #173";
is(sum(2, 2, 2), 6,  '2+2+2');

