#!/usr/bin/perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);

my %opts;
GetOptions(\%opts,
    "help", "start") or exit;

use Alien::SeleniumRC;
if ($opts{help}) {
    Alien::SeleniumRC::help();
    exit;
}
if ($opts{start}) {
    Alien::SeleniumRC::start();
    exit;
}

usage();

sub usage {
    print <<"END_USAGE";
Usage: $0
        --help
        --start
END_USAGE
    exit; 
}
