use strict;
use warnings;

use Test::More tests => 10;

use FindBin;
use lib "$FindBin::Bin/../lib";

use MyTools;


is fibo(1), 1, 'fib 1';
is fibo(2), 1, 'fib 2';
is fibo(3), 2, 'fib 3';
is fibo(4), 3, 'fib 4';
is fibo(5), 5, 'fib 5';

is_deeply fibonacci(1), [1],              'fibs 1';
is_deeply fibonacci(2), [1, 1],           'fibs 2';
is_deeply fibonacci(3), [1, 1, 2],        'fibs 3';
is_deeply fibonacci(4), [1, 1, 2, 3],     'fibs 4';
is_deeply fibonacci(5), [1, 1, 2, 3, 5],  'fibs 5';

