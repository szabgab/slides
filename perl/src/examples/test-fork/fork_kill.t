#!/usr/bin/perl
use strict;
use warnings;

my $pid = fork();

die "fork was not successful\n" if not defined $pid;

if (not $pid) {
    #child
    sleep 100 while(1);
    exit;
}

eval "use Test::More tests => 3";
ok(1);
sleep 1;
ok(1);
kill 9, $pid;
my $stopped = wait();
is($pid, $stopped, "same PID");

