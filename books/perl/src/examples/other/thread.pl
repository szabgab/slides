use strict;
use warnings;

#$| = 0;

use Time::HiRes qw(sleep);
use threads;
#use threads::shared;

my $t = threads->create(\&prt, 3);

foreach my $i (0..4) {
	my $r = rand();
	print "main $$ $i $r\n";
	sleep $r;
}
print "joined: " , $t->join, "\n";

sub prt {
	print "prt  $$ started\n";
	foreach my $i (0..$_[0]) {
		my $r = rand();
		print "prt  $$ $i $r\n";
		sleep $r;
	}
	return 'z';
}
