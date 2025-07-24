#!/usr/bin/perl
use strict;
use warnings;

@ARGV = ("examples/phone_log.txt", "phone_log.txt") if not @ARGV;

while (my $line = <>) {
	next if $line =~ /^\s*$/;   # emtpy lines are acceptable and we skip them
	if ($line =~ /^\[/x) {
		
	} else {
		print "ERROR parsing $ARGV $.\n";
	}
	#[Tue Nov 29 16:21:14 2005] - 45242868767319 - 34918399998432 - voice - end
}
