#!/usr/bin/perl
use strict;
use warnings;

my @resp;
open my $ph, '-|', 'find /' or die;
while (my $line = <$ph>) {
    push @resp, $line;
    last if $line =~ /root/;
}
close $ph;
print @resp;

