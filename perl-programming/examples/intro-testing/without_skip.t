#!/usr/bin/perl
use strict;
use warnings;

use Test::More "no_plan";

like( `/sbin/ifconfig`, qr/eth0/ );
like( `ipconfig`,       qr/Windows IP Configuration/ );

