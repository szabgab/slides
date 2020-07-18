#!/usr/bin/perl
use strict;
use warnings;

package MyServer;
use strict;
use warnings;
use base 'Net::Server';

sub process_request {
    print STDERR "opened\n";
    while (my $line = <STDIN>) {
        print STDERR "$line\n";
    }
}

package main;

use Getopt::Long qw(GetOptions);

my $port = 2000;

GetOptions(
    "port=s" => \$port,
) or die $!;

MyServer->run(
        port   => $port,
        proto  => 'udp',
);



