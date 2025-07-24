#!/usr/bin/perl
use strict;
use warnings;

use Test::Simple "no_plan";

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

open my $fh, '<', "$FindBin::Bin/calc.txt" or die $!;

while ( my $line = <$fh> ) {
    chomp $line;
    next if $line =~ /^\s*(#.*)?$/;

    my ( $exp, $res ) = split /\s*=\s*/, $line;

    ok( mycalc($exp) == $res, $exp );
}

sub mycalc {
    return `$calc @_`;
}

