use strict;
use warnings;

use Test::More tests => 3;


ok(1, "first I");
ok(0, "second II") or BAIL_OUT("no way");
ok(1, "third III");


