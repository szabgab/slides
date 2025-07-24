#!/usr/bin/perl
use strict;
use warnings;

# File globbing
my @xml_files_in_current_dir = glob "*.xml";

my $bin_dir = "/home/foo/bin";
my @perl_files = glob "$bin_dir/*.pl $bin_dir/*.pm";

# my @xml_files_using_old_syntax = <*.xml>;

