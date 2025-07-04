use strict;
use warnings;

use Test::More;
use Test::NoWarnings;

use MyTools qw(add);

plan tests => 4 + 1;

is(add(1, 2), 3,   'first');
is(add(2), 2,      'second');
is(add(3), 3,      'third');
is(add(-1, 1), 0,  'fourth');

