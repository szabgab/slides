#!/usr/bin/perl
use strict;
use warnings;

use Net::Telnet;

my $port = 8000;
my $hostname = 'localhost';

my $telnet = Net::Telnet->new(
                        Port      => $port,
                        Host      => $hostname,
                        Timeout   => 1,
                    );
print "opened\n";

{
    my ($prematch, $match) = $telnet->waitfor('/Username:.*$/');
    if ($prematch =~ /Welcome/) {
        print "welcome printed\n";
    }
    $telnet->print('admin');
}

print "after wait\n";

