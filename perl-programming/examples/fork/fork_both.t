#!/usr/bin/perl
use strict;
use warnings;

my $pid = fork();

die "fork was not successful\n" if not defined $pid;

if (not $pid) {
    #child
    close STDIN;
    close STDERR;
    close STDOUT;
    open STDERR, ">err";
    open STDOUT, ">out";

    open my $out, ">", "child.log" or die "Could not open child.log file";
    open "ok n\n";

    sleep 100;
    exit;
}

eval "use Test::More tests => 5";
ok(1, "first");
sleep 1;
ok(1, "after some sleep");
kill 9, $pid;
my $stopped = wait();
is($pid, $stopped, "same PID");
is(-s "out", 0, "STDOUT of child was empty") and unlink "out";
is(-s "err", 0, "STDERR of child was empty") and unlink "err";

open my $child, "<", "child.log" or die;







