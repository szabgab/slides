use strict;
use warnings;

use Test::More test => 2;

like( `/sbin/ifconfig`, qr/eth0/ );
like( `ipconfig`,       qr/Windows IP Configuration/ );

