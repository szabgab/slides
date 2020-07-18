#!/usr/bin/perl
use strict;
use warnings;

use File::Find;

if (not @ARGV) {
    @ARGV = (".");
}

find (\&find_name, @ARGV);

sub find_name {
    # $File::Find::name looks like: 
    # dir/subdir/subdir/file.ext
    # split at / and at \  for both unix and windows
    my @directories = split m{[/\\]}, $File::Find::name;

    print "  " x (@directories -1); # () needed for precedence
    print "$_\n";
    return;
}

