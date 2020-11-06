use strict;
use warnings;

use lib 'lib';
use MySimpleCalc qw(sum);

use Test::More tests => 1;

isnt(sum(2, 2), 'ERROR',     '2+2' );

