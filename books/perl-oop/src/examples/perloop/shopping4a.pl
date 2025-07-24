#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart4a;

my $foo = Shopping::Cart4a->new('Foo Bar');
print $foo->name, "\n";


