#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart9;

{
    print "Before\n";
    my $foo = Shopping::Cart8->new;
    print "After\n";
}
print "Outside\n";
