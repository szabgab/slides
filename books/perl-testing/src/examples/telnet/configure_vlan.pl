#!/usr/bin/perl
use strict;
use warnings;

use Net::Telnet;

open my $out, ">>", "out.log" or die $!;
my $t = Net::Telnet->new(
        Timeout    => 2,
        #Prompt     => '/>/',
        input_log  => "input.log",
);

$t->open("172.30.40.146");

$t->waitfor('/User:.*$/');
$t->print("admin");

$t->waitfor('/Password:/');
$t->print("");

$t->waitfor('/>/');
$t->prompt('/\(Switching\) >/');
my @lines = $t->cmd("show vlan 5");


if (grep /VLAN ID: 5/, @lines) {
    print "VLAN is already configured\n";
    print "Please remove it manually and rerun the program\n";
    exit;
    #$t->cmd("logout");
}

$t->print("enable");
$t->waitfor('/Password:/');
$t->prompt('/\(Switching\) #/');
$t->print("");

$t->prompt('/\(Switching\) \(Vlan\) #/');
@lines = $t->cmd("vlan database");
@lines = $t->cmd("vlan 5");
#print @lines;
#if (grep /VLAN already/, @lines) {
#   print "QQ 1\n";
#}
@lines = $t->cmd("vlan 5000");
#print @lines;

@lines = $t->cmd("vlan 5");
#print @lines;
#if (grep /VLAN already/, @lines) {
#   print "QQ 2\n";
#}

#@lines = $t->cmd("no vlan 5");
$t->prompt('/\(Switching\) #/');
$t->cmd("exit");



$t->prompt('/--More-- or \(q\)uit/');
@lines = $t->cmd("show ?");

$t->output_record_separator("");
push @lines, $t->cmd(" ");


$t->prompt('/\(Switching\) #show/');
push @lines, $t->cmd(" ");
#print @lines;

$t->output_record_separator("\n");
$t->prompt('/\(Switching\) #/');
@lines = $t->cmd(" vlan 5");  # show was left on the promt line !
#print @lines;

@lines = $t->cmd("show vlan 7");
#print @lines;

@lines = $t->cmd("show slot");
#print @lines;
print $out @lines;



$t->prompt('/\(Switching\) \(Vlan\) #/');
@lines = $t->cmd("vlan database");
@lines = $t->cmd("no vlan 5");
$t->prompt('/\(Switching\) #/');


$t->cmd("exit");
print "done: $_\n";
print $out "done: $_\n";

