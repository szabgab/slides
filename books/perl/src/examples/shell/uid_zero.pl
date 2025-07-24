#!/usr/bin/perl
use strict;
use warnings;

# Look for users with 0 uid

open my $pw, "/etc/passwd" or die "Cannot open /etc/passwd\n";

while (<$pw>) {
    my @items = split /:/;
    if ($items[2] =~ /^0*$/) {
        print ;
    }
}

# Alternatively writen:
#    if ((split /:/)[2] =~ /^0*$/) {



