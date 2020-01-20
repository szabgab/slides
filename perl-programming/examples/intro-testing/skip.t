#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 2;

like( `/sbin/ifconfig`, qr/eth0/ );

SKIP: {
    skip "Windows related tests", 1 if $^O !~ /MSWin/i;
    like( `ipconfig`, qr/Windows IP Configuration/ );
}
