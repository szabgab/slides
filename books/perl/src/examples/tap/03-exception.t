use strict;
use warnings;


use Test::More tests => 5;

diag("planning 5 but running only 3 - with exception");
ok(1, "works");
is(2+2, 4, "2+2 is 4, who would guess ?");
ok(1, "this works again");
die("a real exception");
ok(1);
ok(1);
