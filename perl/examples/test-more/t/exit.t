use strict;
use warnings;

use Test::More tests => 3;

ok(1, "first");
ok(0, "second") or exit;
ok(1, "third");

