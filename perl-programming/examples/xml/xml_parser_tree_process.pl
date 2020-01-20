#!/usr/bin/perl
use strict;
use warnings;

use XML::Parser;

my $parser = XML::Parser->new(Style => 'Tree');
my $tree = $parser->parsefile('examples/data.xml');

# List all the currencies
foreach my $country (get_tag_subtrees($tree->[1], 'country')) {
    my ($name_tree) = get_tag_subtrees($country, 'name');
    my $name = $name_tree->[2];
    foreach my $currency (get_tag_subtrees($country, 'currency')) {
        printf "%-10s %s\n", $name, $currency->[2];
    }
}


# get a country with a given name
foreach my $country (get_tag_subtrees($tree->[1], 'country')) {
    my ($name_tree) = get_tag_subtrees($country, 'name');
    next if $name_tree->[2] ne 'USA';
    foreach my $currency (get_tag_subtrees($country, 'currency')) {
        printf "The currency in the USA is %s.\n", $currency->[2];
    }
}

foreach my $country (get_tag_subtrees($tree->[1], 'country')) {
    next if $country->[0]{id} ne '2';
    foreach my $currency (get_tag_subtrees($country, 'currency')) {
        printf "The currency in the country with id 2 is %s.\n", $currency->[2];
    }
}



sub get_tag_subtrees {
    my ($tree, $name) = @_;

    my @subtrees;

    foreach my $i (1.. (@{ $tree }-1) / 2) {
        if ($tree->[2*$i-1] eq $name) {
            push @subtrees, $tree->[2*$i];
        }
    }
    return @subtrees;
}

