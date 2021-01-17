use strict;
use warnings;

use Test::More tests => 2;

SKIP: {
    skip "Linux related tests", 1 if $^O ne 'linux';
    like( `/sbin/ifconfig`, qr/eth0|enp0s31f6/ );
}

SKIP: {
    skip "Windows related tests", 1 if $^O !~ /MSWin/i;
    like( `ipconfig`, qr/Windows IP Configuration/ );
}
