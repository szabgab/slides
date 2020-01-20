#!/usr/bin/perl
use strict;
use warnings;

my $dir = '.';
if (@ARGV) {
    $dir = $ARGV[0];
}
traverse_dir('', $dir, 0);

sub traverse_dir {
    my ($dir, $thing, $depth) = @_;
    my $path = ($dir ? "$dir/$thing" : $thing);
    print " " x ($depth*3), "$thing\n";
    return if not -d $path;

    if (opendir my $dh, $path) {
        while (my $entry = readdir $dh) {
            next if $entry eq "." or $entry eq "..";
            traverse_dir ($path, $entry, $depth+1);
        }
    } else {
        print " " x ($depth*3-3), "#### Could not open $dir\n";
    }
    return;
}

