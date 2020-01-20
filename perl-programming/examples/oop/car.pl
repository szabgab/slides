#!/usr/bin/perl
use strict;
use warnings;

use IO::Car;

my $c = IO::Car->new;
#print $c;
print $c->data(3), "\n";
print $c->data;
#print $c->get_data(4);

