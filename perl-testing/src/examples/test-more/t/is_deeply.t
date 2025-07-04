use strict;
use warnings;

use Test::More tests => 11;

use MyTools qw(fibo fibonacci);

is fibo(0), 0;
is fibo(1), 1;
is fibo(2), 1;
is fibo(3), 2;
is fibo(4), 3;
is fibo(5), 5;

is_deeply fibonacci(1), [0, 1],              'fibs 1';
is_deeply fibonacci(2), [0, 1, 1],           'fibs 2';
is_deeply fibonacci(3), [0, 1, 1, 2],        'fibs 3';
is_deeply fibonacci(4), [0, 1, 1, 2, 3],     'fibs 4';
is_deeply fibonacci(5), [0, 1, 1, 2, 3, 5],  'fibs 5';
