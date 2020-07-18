#!/usr/bin/perl
use strict;
use warnings;

use Regexp::Common 'RE_ALL';

my $file = 'regexp_common.txt';
if (@ARGV) {
    $file = shift;
}
open(my $data, '<', $file) or die "Could not open $file\n";

while (my $line = <$data>) {
    chomp $line;
    print "LINE: '$line'";
    if ($line =~ RE_balanced(-parens=>'()')) {
        print "  ** balanced parentheses";
    }
    if ($line =~ RE_num_real()) {
        print "  ** a real number";
    }
    if ($line =~ RE_num_int()) {
        print "  ** an integer";
    }
    print "\n";
}


