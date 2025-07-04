#!/usr/bin/perl -w
use strict;

# This script forks several children
$|=1;

my $cnt = $ARGV[0] || 2;


foreach (1..$cnt) {
	my $pid = fork();
	if ($pid) {
		print "In parent $_ pid=$$ after creating child=$pid\n";
	} elsif (defined $pid) {
		print "In child $_  pid=$$\n";
		sleep(rand 5);
		print "In child $_  pid=$$\n";
		exit;
	} else {
		print "In parent, fork failed pid=$$\n";
	}
}

foreach (1..$cnt) {
	wait;
}



