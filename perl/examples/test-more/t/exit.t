use strict;
use warnings;

use Test::More tests => 3;

my $x = 0;

ok(1, "first");
ok($x, "second") or exit;
ok(1, "third");

