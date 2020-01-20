#!/usr/bin/perl

my @people;
$people[0]{name} = 'Foo';
print "$people[0]{name}\n";
$people[0] = 'Bar';
print "$people[0]\n";
$people[0]{name} = 'Baz';
print "$people[0]{name}\n";

use Data::Dumper;
print Dumper \@people;

