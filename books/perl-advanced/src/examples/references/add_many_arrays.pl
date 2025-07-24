#!/usr/bin/perl
use strict;
use warnings;

my @first  = (2, 3);
my @second = (7, 8, 5);
my @third  = (9, 10, 2, 4);
my $res    = add(\@first, \@second, \@third);
print "@$res\n"; # 18 21 7 4

sub add {
    my @args = @_;
    return [] if @args == 0;

    my $longest = 0;
    foreach my $r (@args) {
        if ($longest < @$r) {
            $longest = @$r;
        }
    }

    my @result;
    foreach my $i (0..$longest-1) {
        foreach my $r (@args) {
            $result[$i] += (defined $r->[$i] ? $r->[$i] : 0);
        }
    }
    return \@result;
}

