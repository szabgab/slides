#!/usr/bin/perl
use strict;
use warnings;

use XML::XPath;
my $xml = XML::XPath->new(filename => 'examples/data.xml');
my $name_nodes = $xml->find('/data/country');
foreach my $node ($name_nodes->get_nodelist) {
    my $nn = $node->find('name');
    foreach my $x ($nn->get_nodelist) {
        print XML::XPath::XMLParser::as_string($x);
        print "\n";
    }
}

