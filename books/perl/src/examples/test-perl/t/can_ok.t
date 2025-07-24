use strict;
use warnings;

use Test::More tests => 2;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MyTools;

can_ok('MyTools', 'fibonacci');
can_ok('MyTools', 'make_tea');

