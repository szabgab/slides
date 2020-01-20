#!/usr/bin/perl
use strict;
use warnings;

use DateTime;
# This is UTC time
my $dt = DateTime->now( time_zone => "Asia/Jerusalem");
    #year => 1984,
#    month => 4,
#);


print $dt->ymd, " ", $dt->hms, "\n";
