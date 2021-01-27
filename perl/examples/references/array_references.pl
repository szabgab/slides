#!/usr/bin/env perl
use strict;
use warnings;

my @names = qw(Foo Bar Baz);

my $names_ref  = \@names;
print "$names_ref\n";         # ARRAY(0x703dcf2)

print "@$names_ref\n";        # Foo Bar Baz
print "@{ $names_ref }\n";    # Foo Bar Baz

