#!/usr/bin/perl
use strict;
use warnings;

use Devel::Peek qw(SvREFCNT);
use Data::Dumper();

my @supernames; 
my $more_names;
{
    my $names = [qw(Foo Bar)];
    print SvREFCNT($names), "\n";
    $more_names = $names;
    print SvREFCNT($more_names), "\n";
    @supernames = ($names, $names);
}

print SvREFCNT($more_names), "\n";
print Data::Dumper::Dumper \@supernames;

# Dump( $a );
# DumpArray( 5, $a, $b, ... );
# 

