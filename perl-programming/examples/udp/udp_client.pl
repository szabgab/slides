#!/usr/bin/perl
use strict;
use warnings;

use IO::Socket;
use Getopt::Long qw(GetOptions);

my $MAX_SIZE = 500;
my $port = 2000;
my $host = 'localhost';

GetOptions(
    "port=s" => \$port,
    "host=s" => \$host,
) or die $@;


my $socket = IO::Socket::INET->new(
    Proto     => 'udp',
    PeerPort  => $port,
    PeerAddr  => $host,
) or die $!;

while (my $line = <>) {
    my $msg_in;
    $socket->send($line)              or die "send failed: $!\n";
    $socket->recv($msg_in, $MAX_SIZE) or die "recv() failed: $!\n";

    print $msg_in;
}

$socket->close;
