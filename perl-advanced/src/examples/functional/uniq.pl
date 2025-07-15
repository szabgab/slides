#!/usr/bin/env perl
use strict;
use warnings;
use List::MoreUtils qw(uniq);

my @data = qw(Earth Mars Earth Venus Earth Mars);
my @unique = uniq @data;

print "@unique\n"; # Earth Mars Venus
