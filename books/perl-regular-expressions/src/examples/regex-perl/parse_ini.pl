#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $filename = shift or die "Usage: $0 filename\n";
open my $fh, '<', $filename or die "Could not open '$filename' $!";

my $section;

my %data;

while (my $line = <$fh>) {
    if ($line =~ /^\s*#/) {
        next;        # skip comments
    }
    if ($line =~ /^\s*$/) {
        next;    # skip empty lines
    }

    if ($line =~ /^\[(.*)\]\s*$/) {
        $section = $1;
        next;
    }

    if ($line =~ /^([^=]+?)\s*=\s*(.*?)\s*$/) {
        my ($field, $value) = ($1, $2);
        if (not defined $section) {
            warn "Line outside of seciton '$line'\n";
            next;
        }
        $data{$section}{$field} = $value;
    }
}

print Dumper \%data;
