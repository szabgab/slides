#!/usr/bin/perl
use strict;
use warnings;

my $file = shift or die "Usage: $0 FILENAME\n";
open my $fh, '<', $file or die;
print "Press any key to close file and script";
<STDIN>;

