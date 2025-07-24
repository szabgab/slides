#!/usr/bin/perl -w
use strict;

use Net::Telnet;

open my $out, ">>", "out.log" or die;
my $t = Net::Telnet->new(
		Timeout    => 2,
		input_log  => "input.log",
);

$t->open("80.80.80.63");


$t->waitfor('/PE-South>$/');
$t->print("enable");
$t->waitfor('/Password:.*$/');
$t->print("admin");
$t->waitfor('/PE-South#$/');

$t->prompt('/PE-South#/');
my @lines = $t->cmd("show ip vrf");
print @lines;
