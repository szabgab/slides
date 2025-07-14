#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper qw(Dumper);

use Config::Tiny;

my $filename = shift or die "Usage: $0 filename\n";
open my $fh, '<', $filename or die "Could not open '$filename' $!";

my $data = Config::Tiny->read( $filename );

print Dumper $data;
