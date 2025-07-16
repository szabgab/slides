#!/usr/bin/perl
use strict;
use warnings;

use Acme::EyeDrops qw(sightly);
my $filename = shift or die "Usage: $0 FILENAME\n";

print sightly( { 
                Shape       => "camel",
                SourceFile  => $filename,
               } );

