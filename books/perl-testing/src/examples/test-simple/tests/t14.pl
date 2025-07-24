use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MySimpleCalc qw(sum);

use Test::Simple tests => 3;

ok(sum(1, 1)==2,     '1+1');
ok(sum(2, 2)==4,     '2+2');
ok(sum(2, 2, 2)==6,  '2+2+2');
