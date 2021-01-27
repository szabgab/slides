#!/usr/bin/env perl
use strict;
use warnings;

my @first  = (2, 3);
my @second = (7, 8, 5);
my @res    = add(\@first, \@second);  # passing two references
print "@res\n";

sub add {
    my ($one_ref, $two_ref) = @_;
    my @one = @{ $one_ref };       # dereferencing and copying each array
    my @two = @{ $two_ref };

    my @result;
    foreach my $i (0..@one-1) {
        if (defined $two[$i]) {
            push @result, $one[$i] + $two[$i];
        }
        else {
            push @result, $one[$i];
        }
    }
    foreach my $i (@one..@two-1) {
        push @result, $two[$i];
    }
    return @result;
}

