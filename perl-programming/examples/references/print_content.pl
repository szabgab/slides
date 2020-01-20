#!/usr/bin/perl
use strict;
use warnings;

my @names     = qw(Foo Bar Baz);
my $names_ref = \@names;

my %phones = (
    Barney  => 123,
    Fred    => 456,
    Wilma   => 789,
);
my $phones_ref = \%phones;

print $names_ref, "\n";         # ARRAY(0x703dcf2)
print "@{ $names_ref }\n";      # Foo Bar Baz
print $phones_ref, "\n";        # HASH(0x703fed1)
print %{ $phones_ref }, "\n";;  # Fred456Barney123Wilma789,

