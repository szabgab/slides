#!/usr/bin/perl -w
use strict;

my $numbering = 0;           # true if -n received
my $end_sign = 0;            # true if -E received

my @files=();                # list of files to process


# process the arguments
while (my $arg = shift @ARGV) {
	if ($arg eq "-n") { 
		$numbering = 1;
	} else {
		if ($arg eq "-E") {
			$end_sign = 1;
		} else {
			push @files , $arg;
		}
	}
}

my $counter = 0;                # line counter
while (@files) {
	@ARGV = (shift @files);     # field the ARGV one-by-one with the filenames
	while (<>) {
		if ($numbering) {
			$counter++;
			print "$counter  ";
		}
		print;
	}
	if ($end_sign) {
		print "\$\n";
	}
}

