#!/usr/bin/perl
use strict;
use warnings;

f("hello", "world");

AUTOLOAD {
    our $AUTOLOAD;
    print "$AUTOLOAD\n";
    print "@_\n";
}
