#!/usr/bin/env perl
use strict;
use warnings;

use XML::Simple qw(XMLin);

my $xml = XMLin("examples/simple.xml", ForceArray => 1);
#use Data::Dumper qw(Dumper);
#print Dumper $xml;
#exit;

print join "-", keys %{$xml->{person}};
print "\n";

foreach my $id (keys %{$xml->{person}}) {
    printf "%-10s %-10s %-10s\n",
        $xml->{person}{$id}{fname}[0],
        $xml->{person}{$id}{lname}[0],
        $xml->{person}{$id}{idnum}[0];
}

