#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart2_2;

my $foo = Shopping::Cart2_2->new;
$foo->set_name('Foo');
