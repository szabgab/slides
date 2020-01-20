use strict;
use warnings;

use Test::More;
use Test::NoWarnings;

plan tests => 4 + 1;


ok(1, 'first');
ok(2 + 'a', 'second');
ok(3 + 'b', 'third');
ok(4, 'fourth');

