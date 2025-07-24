#!/usr/bin/perl
use strict;
use warnings;

my $n = shift or die "Usage: $0 NUMBER\n";

my $result = factorial($n);
print $result;

sub factorial {
    my ($n) = @_;
    if ($n == 1) {
        return 1;
    }
    my $prev = factorial($n - 1);
    return $n * $prev;
}
