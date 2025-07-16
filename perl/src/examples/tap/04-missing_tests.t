use strict;
use warnings;


use Test::More tests => 5;

diag("planning 5 but running only 3");
ok(1, "works");
is(2+2, 4, "2+2 is 4, who would guess ?");
ok(1, "this works again");
exit(0);
ok(1);
ok(1);
