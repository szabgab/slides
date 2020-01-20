#!/usr/bin/perl

use File::Find 'find';

find({
    wanted   => \&old_files,
    no_chdir => 1,
    }, $ARGV[0] || '.');

sub old_files {
     print "$_\n" if -M $_ > 3;
}
