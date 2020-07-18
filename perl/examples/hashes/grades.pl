#!/usr/bin/perl
use strict;
use warnings;

my %grades;
$grades{"Foo Bar"}{Mathematics}   = 97;
$grades{"Foo Bar"}{Literature}    = 67;
$grades{"Peti Bar"}{Literature}   = 88;
$grades{"Peti Bar"}{Mathematics}  = 82;
$grades{"Peti Bar"}{Art}          = 99;

#foreach my $name (sort keys %grades) {
#    foreach my $subject (keys %{$grades{$name}}) {
#        print "$name, $subject: $grades{$name}{$subject}\n";
#    }
#}

use Data::Dumper qw(Dumper);

print Dumper \%grades;
