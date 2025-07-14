#!/usr/bin/perl
use strict;
use warnings;


my %a = (
    myself => 'a'
);
my %b = (
    myself => 'b',
);


$a{b} = \%b;
$b{a} = \%a;

use Data::Dumper;
print Dumper \%a, \%b;

