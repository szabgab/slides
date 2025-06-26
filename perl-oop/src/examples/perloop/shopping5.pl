#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart5;

my $foo = Shopping::Cart5->new;
$foo->add('The OOP book of Damian');

use Data::Dumper;

print Dumper $foo;

