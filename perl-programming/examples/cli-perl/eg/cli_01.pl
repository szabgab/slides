#!/usr/bin/perl
use strict;
use warnings;

use Net::Telnet;

my $port = 8000;
my $hostname = 'localhost';

my $telnet = Net::Telnet->new(
                        Port      => $port,
                        Host      => $hostname,
                    );
print "opened\n";

{
    my ($prematch, $match) = $telnet->waitfor('/not likely to show up/');
}

print "after wait\n";

