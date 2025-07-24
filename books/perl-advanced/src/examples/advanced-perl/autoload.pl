#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper qw(Dumper);

f("hello", "world");

AUTOLOAD {
    our $AUTOLOAD;
    print "$AUTOLOAD\n";
    print Dumper \@_;
}
