#!/usr/bin/perl
use strict;
use warnings;

use XML::Parser;
use Data::Dumper;

my $parser = XML::Parser->new(Style => 'Tree');
my $tree = $parser->parsefile('examples/data.xml');

$Data::Dumper::Indent = 0;
print Dumper $tree;

__END__
print "\n----------------\n";
print "$tree->[0]\n";             #   data

print "$tree->[1][3]\n";          #   country
print "$tree->[1][4][0]{id}\n";   #   1
print "$tree->[1][4][3]\n";       #   name
print "$tree->[1][4][4][2]\n";    #   USA
print "$tree->[1][4][7]\n";       #   languages

print "$tree->[1][7]\n";          #   country

