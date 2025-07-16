#!/usr/bin/perl
use strict;
use warnings;

if (open my $fh, '<', "other_data.txt") {
    # should do here something
} else {
    warn $!;
}
