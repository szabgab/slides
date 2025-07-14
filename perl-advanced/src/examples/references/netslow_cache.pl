#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/references';
use NetSlow qw(compute);
use YAML qw(DumpFile LoadFile);

die "Need 2 numbers\n" if @ARGV != 2;

my $cache_file = "netslow_cache.yml";
my $cache;

if (-e $cache_file) {
    $cache = LoadFile($cache_file);
}
my ($x, $y) = @ARGV;
my $result;

if (not defined $cache->{$x}{$y}) {
    $cache->{$x}{$y} = compute($x, $y);
}
DumpFile($cache_file, $cache);
print $cache->{$x}{$y}, "\n";

