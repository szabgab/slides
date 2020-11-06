use strict;
use warnings;

use lib 'lib';
use MySimpleCalc qw(sum);

use Test::More tests => 3;

is(sum(1, 1),    2,     '1+1'   );
is(sum(2, 2),    4,     '2+2'   );
is(sum(2, 2, 2), 6,     '2+2+2' );

