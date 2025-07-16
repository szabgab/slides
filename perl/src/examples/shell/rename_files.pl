#!/usr/bin/perl
use strict;
use warnings;

foreach my $file (glob "*.xml") {
    my $new = substr($file, 0, -3) . "html";
    rename $file, $new;
}

