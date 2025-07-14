#!/usr/bin/perl
use strict;
use warnings;

my $names_ref = [qw(Foo Zorg)];

# copy the ARRAY reference, the content is the same location
my $names_other_ref  = $names_ref;
$names_other_ref->[0] = 'Bar';
print "$names_other_ref->[0]\n";    # Bar
print "$names_ref->[0]\n";          # Bar
print "$names_ref\n";
print "$names_other_ref\n";

# copy the content of the ARRAY reference
my $names_yet_other_ref = [ @{$names_ref} ];
$names_yet_other_ref->[0] = 'Moo';
print "$names_yet_other_ref->[0]\n";    # Moo
print "$names_ref->[0]\n";              # Bar 
print "$names_other_ref->[0]\n";        # Bar
print "$names_yet_other_ref\n";

