#!/usr/bin/perl
use strict;
use warnings;

use Net::Telnet ();
my $t = Net::Telnet->new();
 
$t->open('localhost');
$t->login('smoke', '123456');
my @lines = $t->cmd("who");
print @lines;
print "\n";

print "Who am i: ", $t->cmd("whoami"), "\n\n";
