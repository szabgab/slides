#!/usr/bin/perl 
use strict;
use warnings;

my $line = "named:x:44:66:Nameserver Daemon:/var/named:/bin/bash";

my @fields = split ":", $line;         # fetch 3 values like this
my $uid  = $fields[2];
my $gid  = $fields[3];
my $home = $fields[5];

($uid, $gid, $home) = @fields[2,3,5];

($uid, $gid, $home) = (split ":", $line)[2,3,5];  # or like this
print "uid:  $uid\n";
print "gid:  $gid\n";
print "home: $home\n";
