#!/usr/bin/perl
use strict;
use warnings;

print "Process ID: $$\n";

$SIG{INT} = sub { print "\nINT - I don't want to die!!!\n" };
$SIG{TERM} = sub { print "\nTERM - Don't terminate me!!!\n" };

$SIG{TSTP} = sub { print "\nTTP - No background check for me!!!\n" };

sleep 1 while 1;
