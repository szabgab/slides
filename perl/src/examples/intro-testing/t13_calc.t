#!/usr/bin/perl
use strict;
use warnings;

use Test::Simple "no_plan";

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

open my $fh, '<', "$FindBin::Bin/calc.txt" or die $!;

while ( my $line = <$fh> ) {
    chomp $line;
    next if $line =~ /^\s*$/;
    next if $line =~ /^#/;

    my ( $exp, $res ) = split /\s*=\s*/, $line;

    ok( `$calc $exp` == $res, $exp );
}

