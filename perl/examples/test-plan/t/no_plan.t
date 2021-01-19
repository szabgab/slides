use strict;
use warnings;

use Fibonacci qw(fibo);

use Test::More 'no_plan';

is fibo(1), 1;
is fibo(2), 1;
is fibo(3), 2;
is fibo(4), 3;
is fibo(5), 5;
is fibo(6), 8;
