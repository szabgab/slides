#!/usr/bin/perl
use strict;
use warnings;

my $pid = fork();

die "fork was not successful\n" if not defined $pid;

if (not $pid) {
    #child
    sleep 3;
    exit;
}

eval "use Test::More tests => 3";
ok(1);
sleep 1;
ok(1);
ok(1);

