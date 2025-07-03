use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MyFibo qw(fibo);

use Test::Simple tests => 9;

ok( fibo(0) == 0 );
ok( fibo(1) == 1 );
ok( fibo(2) == 1 );
ok( fibo(3) == 2 );
ok( fibo(4) == 3 );
ok( fibo(5) == 5 );
ok( fibo(6) == 8 );

# what should these really be?
ok( fibo(7.5) == 13);
ok( fibo(-8)  == 1);
