use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 3;

diag last_update();
ok( last_update() =~
    /^This page was last updated at/, 'last_update =~');

like( last_update(),
    qr/^This page was last updated at/, 'last_update like');

like( last_update(),
    qr/^This page was last updated at \d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d$/, 'last_update full match');

