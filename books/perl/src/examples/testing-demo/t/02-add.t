use strict;
use warnings;

use Test::More;
use MyMath qw(add);

is add(2, 2), 4;
is add(2, 3), 5;
is add(0, 0), 0;

done_testing;

