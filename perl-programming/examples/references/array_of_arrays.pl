#!/usr/bin/perl
use strict;
use warnings;

my $first_names_ref  = [ qw(Foo Bar Baz) ];
my $family_names_ref = [ qw(Moo Zorg) ];

my @names = ($first_names_ref, $family_names_ref);

print "$first_names_ref\n";       # ARRAY(0x703dcf2)
print "@{ $first_names_ref }\n";  # Foo Bar Baz

print "$names[0]\n";              # ARRAY(0x703dcf2)
print "@{ $names[0] }\n";         # Foo Bar Baz
print "@{ $names[1] }\n";         # Moo Zorg

print "$first_names_ref->[0]\n";  # Foo
print "$names[0]->[0]\n";         # Foo

print "$names[0][0]\n";           # Foo

