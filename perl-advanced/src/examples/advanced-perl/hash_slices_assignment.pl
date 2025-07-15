#!/usr/bin/perl 
use strict;
use warnings;


my @fields = qw(fname lname phone);

my @values = qw(Peti Bar 12345);

my %h;
@h{@fields} = @values;


print "$h{fname}\n";   # Peti
print "$h{lname}\n";   # Bar
print "$h{phone}\n";   # 12345
