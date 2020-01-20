#!/usr/bin/perl
use strict;
use warnings;


sub add {
    my ($x, $y) = @_;
    return $x+$y;
}

sub multiply {
    my ($x, $y) = @_;
    return $x*$y;
}

my %dispatch = (
    '+'  => 'add',
    '*'  => 'multiply',
);

my $op = '+';

# Generally not recommended to use symbolic references!!
# unless you really know what are you doing
{
    no strict 'refs';
    print $dispatch{$op}->(2, 3), "\n";
}

