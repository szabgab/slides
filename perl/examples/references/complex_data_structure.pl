#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my %grades;
$grades{"Foo Bar"}{Mathematics}   = 97;
$grades{"Foo Bar"}{Literature}    = 67;
$grades{"Peti Bar"}{Literature}   = 88;
$grades{"Peti Bar"}{Mathematics}  = 82;
$grades{"Peti Bar"}{Art}          = 99;
$grades{"Foo Bar"}{Chemistry}[0]  = 30;
$grades{"Foo Bar"}{Chemistry}[1]  = 48;
$grades{"Foo Bar"}{Chemistry}[2]  = 72;
$grades{"Foo Bar"}{Chemistry}[3]  = 80;

print Dumper \%grades;

