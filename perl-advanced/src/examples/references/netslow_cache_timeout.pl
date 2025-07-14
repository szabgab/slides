#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/references';
use NetSlow qw(compute);
use YAML qw(DumpFile LoadFile);

die "Need 2 numbers\n" if @ARGV != 2;

my $cache_file = "netslow_cache_timeout.yml";
my $cache;

if (-e $cache_file) {
    $cache = LoadFile($cache_file);
}
my ($x, $y) = @ARGV;
my $result;

my $TIMEOUT = 5;

if (not defined $cache->{$x}{$y} or
    $cache->{$x}{$y}{timestamp} < time() - $TIMEOUT ) {
    $cache->{$x}{$y}{value} = compute($x, $y);
    $cache->{$x}{$y}{timestamp} = time;
}
DumpFile($cache_file, $cache);
print $cache->{$x}{$y}{value}, "\n";

