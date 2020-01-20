#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::RestrictedCart;

eval {
    my $foo = Shopping::RestrictedCart->new;
};
print "ERROR: $@";


my $bar = Shopping::RestrictedCart->new(restriction => 25, name => 'Bar');
$bar->add_item('The OOP book of Damian');
printf "Current price for %s is %s\n", $bar->get_name, $bar->get_price();
$bar->add_item('The OOP book of Damian');
printf "Current price for %s is %s\n", $bar->get_name, $bar->get_price();

