use strict;
use warnings;

use Test::More;

plan tests => 3;

use_ok('App');

ok(App::add(1, 1) == 2, "1+1 = 2");

is(App::add(2, 3),  5, "2+3 = 5");



