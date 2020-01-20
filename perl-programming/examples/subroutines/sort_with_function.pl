#!/usr/bin/perl
use strict;
use warnings;

my @data = qw(foo Foo Bar Moo FooBar Name Moose Apple Ape More Peach);
my @sorted = sort by_length @data;

print "@data\n";
print "@sorted\n";

# foo Foo Bar Moo FooBar Name Moose Apple Ape More Peach
# Ape Bar Foo foo Moo More Name Apple Moose Peach FooBar

sub by_length {
    length($a) <=> length($b)
    or
    lc($a) cmp lc($b)
    or
    $a cmp $b
}
