#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my $filename = shift 
    or die "Usage: $0 FILENAME ( examples/references/data.ini )\n";

my %ini;
my $section = '';
open my $fh, '<', $filename or die;
while (my $line = <$fh>) {
    chomp $line;
    next if $line =~ /^\s*(#.*)?$/;
    if ($line =~ /^\[(.*)\]/) {
        $section = $1;
        next;
    }
    if ($line =~ /^(\w+)\s*=\s*(.*)$/) {
        $ini{$section}{$1} = $2;
        next;
    }
}

print Dumper \%ini;

