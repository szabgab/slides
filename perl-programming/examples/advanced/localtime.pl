#!/usr/bin/perl
use strict;
use warnings;

my $t = time;

my $lt = localtime($t);
print "$lt\n";       # Fri May 20 11:26:23 2011

my @time = localtime($t);    
print "@time\n";     # 23 26 11 20 4 111 5 139 1

