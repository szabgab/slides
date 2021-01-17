use strict;
use warnings;

use Test::More 'no_plan';

use MyMath qw(add div fibo);

is(add(2, 3), 5);

#is(fibo(0), 0);
#is(fibo(1), 1);
#is(fibo(2), 1);
#is(div(6, 3), 2);

#is(div(6, 0), 0);
#is(fibo(-1), -1);
