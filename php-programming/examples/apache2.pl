#!/usr/bin/env perl
use strict;
use warnings;

use POSIX ();
use FindBin;

$ENV{APACHE_PID_FILE} = '/tmp/apache.pid';
$ENV{APACHE_RUN_USER} = $ENV{APACHE_RUN_GROUP} = POSIX::cuserid();
$ENV{COURSE_DIR} = "$FindBin::Bin/..";


my $mode = shift;
die "Usage: $0 [start|stop]\n"
	unless $mode and ($mode eq 'start' or $mode eq 'stop');

system  "apache2 -f $FindBin::Bin/apache2.conf -k $mode";
if ($mode eq 'start') {
	print "Access via http://localhost:8081/\n";
}

