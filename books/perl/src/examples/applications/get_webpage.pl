#!/usr/bin/env perl
use strict;
use warnings;

use LWP::Simple qw(get);

my $page = get "http://perlmaven.com/";
if ($page) {
    print "Site is alive\n";
} else {
    print "Site is not accessible\n";
}

