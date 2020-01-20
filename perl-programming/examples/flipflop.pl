#!/usr/bin/perl
use strict;
use warnings;

foreach my $i (1,1,1, 2,2,2, 3,3,3) {
	print "$i\n";
	if ($i == 2 .. $i ==2) {
		print "in\n";
	}

}


