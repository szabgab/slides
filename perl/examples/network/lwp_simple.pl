#!/usr/bin/perl
use strict;
use warnings;

my $url = 'http://localhost:5000/';
if (defined $ARGV[0]) {
    $url = $ARGV[0];
}

use LWP::Simple qw(get);

my $page = get($url);
if (defined $page) {
    print $page;
} else {
    print "Could not fetch $url\n";
}
print "\n";

