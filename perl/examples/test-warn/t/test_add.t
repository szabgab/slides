use strict;
use warnings;

use Test::More;

use MyTools qw(add);

plan tests => 4;

is(add(1, 2), 3,   'first');
is(add(2, 'a'), 2, 'second');
is(add('b', 3), 3, 'third');
is(add(-1, 1), 0,  'fourth');

