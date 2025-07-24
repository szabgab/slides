#!/usr/bin/perl
use strict;
use warnings;

use File::Copy qw(move);

foreach my $file (glob "*.xml") {
    my $new = substr($file, 0, -3) . "html";
    print "move $file, $new\n";
    #move $file, $new;
}

