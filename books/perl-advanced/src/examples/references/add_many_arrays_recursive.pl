#!/usr/bin/env perl
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

    my $first = shift @args;
    if (@args) {
        my $rest = add(@args);
        return add2($first, $rest);
    } else {
        return [@$first];
    }
}


# is the same as was the add() in add_arrays_nocopy_return.pl
sub add2 {
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
    return \@result;
}

