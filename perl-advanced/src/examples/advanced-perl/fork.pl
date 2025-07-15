
use strict;
use warnings;

use POSIX ":sys_wait_h";

my $pid = fork();
if (not defined $pid) {
   die "Could not fork";
}

if ($pid) {
    # parent
    # wait till the child exists and then continue
	my $kid;
    print "in parent of $pid\n";
	do {
    	$kid = waitpid($pid, WNOHANG);
		sleep 1;
	} while $kid != $pid;
	print "arrived $kid\n";
} else {
	print "in child\n";
	# Expect->new
    #...
    # till the end of expect
	sleep 5;
    print "done\n";
	exit;
}

print "next\n";
