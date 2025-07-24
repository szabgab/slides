#!/usr/bin/env perl
use strict;
use warnings;

my @names = (
    [ qw(Foo Bar Baz) ],
    [ qw(Moo Zorg) ],
);

print "$names[0]\n";              # ARRAY(0x703dcf2)
print "@{ $names[0] }\n";         # Foo Bar Baz
print "@{ $names[1] }\n";         # Moo Zorg

print "$names[0]->[0]\n";         # Foo
print "$names[0][0]\n";           # Foo

