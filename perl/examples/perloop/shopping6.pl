#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart6;

my $foo = Shopping::Cart6->new;
$foo->add('The OOP book of Damian');
my $name = 'The OOP book of Damian';
printf "Number of '%s' items in cart is %s\n",
        $name, $foo->get($name);

