#!/usr/bin/env perl
use strict;
use warnings;

my %phones = (
    Barney  => 123,
    Fred    => 456,
    Wilma   => 789,
);
my $phones_ref = \%phones;

print $phones_ref, "\n";             # HASH(0x703fed1)
my @names = sort keys %$phones_ref};
print "@names\n";                    # Barney Fred Wilma

print "$phones{Fred}\n";             # 456
print "$phones_ref->{Fred}\n";       # 456
