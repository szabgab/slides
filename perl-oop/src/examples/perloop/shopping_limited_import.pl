#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::LimitedCartImport limit => 2;

my @carts;
foreach (1..4) {
    push @carts, Shopping::LimitedCartImport->new;
}
printf("After 4th: %s %s\n",
    Shopping::LimitedCartImport->get_object_count(),
    Shopping::LimitedCartImport->get_existing_object_count());

