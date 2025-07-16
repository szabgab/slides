#!/usr/bin/perl
use strict;
use warnings;

use XML::LibXML;

my $parser = XML::LibXML->new;
my $doc = $parser->parse_file('examples/data.xml');
print $doc;

process_node( $doc->getDocumentElement, 0);

sub process_node {
    my ($node, $depth) = @_;
    print "$node\n";
    return unless( $node->nodeType eq &XML_ELEMENT_NODE );
    print "  " x $depth, $node->nodeName, "\n";
    foreach my $child ( $node->getChildnodes ) {
        process_node( $child, $depth+1 );
    }
}



