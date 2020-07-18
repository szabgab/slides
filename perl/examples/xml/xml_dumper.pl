#!/usr/bin/perl
use strict;
use warnings;

use XML::Dumper;

open my $out, '>', 'out.xml' or die;

my $dumper = XML::Dumper->new();

my $perl = {
    people => [
        {
            name => 'Foo',
            phone => 123,
        },
        {
            name => 'Bar',
            phone => 456,
        },
        {
            name => 'Baz',
            phone => 789,
        },
    ],
};

my $xml = $dumper->pl2xml($perl);
print $xml;

my $perl_again = $dumper->xml2pl( $xml );
use Data::Dumper;
print Dumper $perl, $perl_again;

