use strict;
use warnings;

use Test::More;
my $tests;

plan tests => $tests;

use FindBin;
use lib "$FindBin::Bin/../lib";

use MyTools;

{
    is sum(2, 2), 4, '2 + 2 = 4';

    TODO: {
        local $TODO = "teach it to add more than 2 numbers";
        is sum(2, 2, 2), 6, '2 + 2 + 2 = 6';
    }

    BEGIN { $tests += 2; }
}

{
    is fibonacci(1), 1, 'fib 1';
    is fibonacci(2), 1, 'fib 2';
    is fibonacci(3), 2, 'fib 3';
    is fibonacci(4), 3, 'fib 4';
    is fibonacci(5), 5, 'fib 5';

    is_deeply [ fibonacci(1) ], [1],              'fibs 1';
    is_deeply [ fibonacci(2) ], [1, 1],           'fibs 2';
    is_deeply [ fibonacci(3) ], [1, 1, 2],        'fibs 3';
    is_deeply [ fibonacci(4) ], [1, 1, 2, 3],     'fibs 4';
    is_deeply [ fibonacci(5) ], [1, 1, 4, 3, 5],  'fibs 5'; # bug added on purpose

    BEGIN { $tests += 10; }
}

{
    TODO: {
        local $TODO = 'fix multiply';
        is multiply(), 0, 'nothing should be 0';
    }

    is multiply(1),      1, 'one';
    is multiply(1, 1),   1, '1 * 1';
    is multiply(1, -1), -1, '1 * -1';
    is multiply(-1, -1), 1, '-1 * -1';
    BEGIN { $tests += 5; }
}

