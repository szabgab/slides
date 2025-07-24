#!/usr/bin/env perl
use strict;
use warnings;

my @first  = (2, 3);
my @second = (7, 8, 5);
my @res    = add(\@first, \@second);
print "@res\n";

sub add {
    my ($one_ref, $two_ref) = @_;

    my @result;
    foreach my $i (0..@{ $one_ref }-1) {
        if (defined $two_ref->[$i]) {
            push @result, $one_ref->[$i] + $two_ref->[$i];
        }
        else {
            push @result, $one_ref->[$i];
        }
    }
    foreach my $i (@{ $one_ref }..@{ $two_ref }-1) {
        push @result, $two_ref->[$i];
    }
    return @result;
}

