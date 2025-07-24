use strict;
use warnings;

use Test::More;
use Test::Exception;

use MyTools qw(fibo);

is fibo(6), 8, 'fibo(6)';

throws_ok { fibo() } qr/Need to get a parameter/, 'missing parameter';
throws_ok { fibo('name') } qr/Need to get a number/, 'not a number';

done_testing;
