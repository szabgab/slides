#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart7;

my @users;
my $c = Shopping::Cart7->new;
$c->set_name('Foo');
$c->add_item('The OOP book of Damian');
printf "Current price for %s is %s\n", $c->get_name, $c->get_price();


