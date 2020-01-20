#!/usr/bin/perl
use strict;
use warnings;

my $threshold = 0.01;

open my $fh, "/proc/loadavg" or die "Cannot read /proc/loadavg\n";
my $line = <$fh>;
my $load = (split " ", $line)[0];
if ($load > $threshold) {
    system "/usr/bin/logger", "-p", "crit", "High LOAD: $load\n";
}

# you can add here the code for logging in a file and sending e-mail
# but be careful as if the load if high you won't be able to send the
# email.


