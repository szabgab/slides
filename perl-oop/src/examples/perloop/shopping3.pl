#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart3;

my $foo = Shopping::Cart3->new;
$foo->name('Foo');
print $foo->name, "\n";
