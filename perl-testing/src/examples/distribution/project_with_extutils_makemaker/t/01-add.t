use strict;
use warnings;

use Test::Simple tests => 1;

use MyTools qw(add);

ok(add(2, 3) == 5, 'adding two numbers');
