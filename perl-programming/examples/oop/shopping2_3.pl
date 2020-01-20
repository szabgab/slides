#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart2_3;

my $foo = Shopping::Cart2_3->new;
$foo->set_name('Foo');
print $foo->get_name(), "\n";
