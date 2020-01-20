use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";

use Test::More tests => 2;
use Test::Trap;

use MyTools;

my @r = trap { call_exit(2); };
is( $trap->exit, 2, 'exit(2) called' );

ok(1, "after calling exit");


