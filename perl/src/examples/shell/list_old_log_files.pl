#!/usr/bin/perl
use strict;
use warnings;

use File::Find 'find';

find({
    wanted   => \&old_files,
    no_chdir => 1,
}, $ARGV[0] || '.');

sub old_files {
    if (substr($_, -4) ne ".log") {
        return;
    }
    if (-M $_ > 3) {
        print "$_\n";
    }
    return;
}

