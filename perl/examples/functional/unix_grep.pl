#!/usr/bin/perl
use strict;
use warnings;

my $regex = shift;
print grep { $_ =~ /$regex/ } <>;

