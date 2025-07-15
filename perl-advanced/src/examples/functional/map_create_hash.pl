#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper qw(Dumper);

my @words = qw(Foo Bar Baz);

my %copy_paste = (Foo => 1, Bar => 1, Baz => 1);

my %lookup = map {$_ => 1} @words;

print Dumper \%copy_paste;
print Dumper \%lookup;

# $VAR1 = {
#           'Bar' => 1,
#           'Baz' => 1,
#           'Foo' => 1
#         };
