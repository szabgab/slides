#!/usr/bin/env perl
use strict;
use warnings;

use Filesys::DiskUsage qw(du);

if (not @ARGV) {
    die "Usage: $0 DIRs\n";
}

my %sizes = du({'make-hash' => 1}, @ARGV);
foreach my $entry (sort { $sizes{$a} <=> $sizes{$b} } keys %sizes) {
    print "$entry => $sizes{$entry}\n";
}

