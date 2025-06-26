#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart4;

my $foo = Shopping::Cart4->new('Foo Bar');
print $foo->name, "\n";

