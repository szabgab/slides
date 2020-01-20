#!/usr/bin/perl
use strict;
use warnings;

use XML::Simple;# qw(:strict);
use Data::Dumper;
my $xml = XMLin('examples/data.xml',
        ForceArray => 0, 
        KeyAttr => [],
        );
print Dumper $xml;

